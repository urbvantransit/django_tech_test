docker-compose down -v
docker-compose up --build -d postgres

sleep 10

docker-compose up --build -d proxy
docker-compose logs -f django_prod
