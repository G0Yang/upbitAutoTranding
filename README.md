
# Build docker image
docker build -t upbit_auto_trading .

# Run api server
docker-compose up -d

# Stop api server
docker-compose down