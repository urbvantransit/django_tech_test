#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
# http://stackoverflow.com/questions/19622198/what-does-set-e-mean-in-a-bash-script
set -e

# Check if the required PostgreSQL environment variables are set

# Used by docker-entrypoint.sh to start the dev server
# If not configured you'll receive this: CommandError: "0.0.0.0:" is not a valid port number or address:port pair.
[ -z "$PORT" ] && echo "ERROR: Need to set PORT. E.g.: 8000" && exit 1;

[ -z "$POSTGRES_DB" ] && echo "ERROR: Need to set POSTGRES_NAME" && exit 1;
[ -z "$POSTGRES_USER" ] && echo "ERROR: Need to set POSTGRES_USER" && exit 1;
[ -z "$POSTGRES_PASSWORD" ] && echo "ERROR: Need to set POSTGRES_PASSWORD" && exit 1;


# Define help message
show_help() {
    echo """
Usage: docker run <imagename> COMMAND

Commands

dev             : Start a normal Django development server
bash            : Start a bash shell
manage          : Start manage.py
setup_database  : Restart to a known point
python          : Run a python command
uwsgi           : Run uwsgi server
tox             : Run tests and check PEP8
help            : Show this message
"""
}

write_uwsgi() {
    echo "Generating uwsgi config file..."
    snippet="import os;
import sys;
import jinja2;
sys.stdout.write(jinja2.Template(sys.stdin.read()).render(env=os.environ))"

    cat /usr/src/ops/uwsgi.ini | python -c "${snippet}" > /uwsgi.ini
}

# Run
case "$1" in
    dev)
        echo "Running Development Server on 0.0.0.0:${PORT}"
        python manage.py runserver 0.0.0.0:${PORT}
    ;;
    bash)
        /bin/bash "${@:2}"
    ;;
    manage)
        python manage.py "${@:2}"
    ;;
    setup_database)
        python manage.py makemigrations
        python manage.py makemigrations lines stations
        python manage.py migrate
    ;;
    python)
        python "${@:2}"
    ;;
    uwsgi)
        # Used by uwsgi.ini file to start the wsgi Django application
        [ -z "$WSGI_MODULE" ] && echo "ERROR: Need to set WSGI_MODULE. E.g.: hello.wsgi:application" && exit 1;
        
        echo "Running App (uWSGI)..."
        write_uwsgi
        uwsgi --ini /uwsgi.ini
    ;;
    check_pep8)
        flake8 apps urbvan urbvan_framework --exclude=settings,__init__.py,migrations
    ;;
    test)
        python manage.py test --parallel 3 --settings=urbvan.settings.local
    ;;
    *)
        show_help
    ;;
esac
