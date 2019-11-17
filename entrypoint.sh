#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
	echo "ESPERANDO POR POSTGRES..."
	while ! nc -z $SQL_HOST $SQL_PORT; do
		sleep 0.1
	done

	echo "SE HA INICIADO POSTGRES * HOLAAAA DHARWIN * "
fi

python manage.py flush --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput --clear

exec "$@"