docker-compose down -v
docker-compose up --build -d django_dev
docker-compose logs -f django_dev
