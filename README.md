
# configure .env
```
cp .env.sample .env
```

# make venv for dev
```
cd src
python3 -m venv venv
```

# activate venv
```
cd src
source venv/bin/activate
```

# deactivate venv
```
deactivate
```

# install requirements
```
python -m pip install -r requirements.txt
```

# run server on localhost
```
python runServer.py
```

# Build docker image
```
docker build -t upbit_auto_trading .
```

# Run api server
```
docker-compose up -d
```

# Stop api server
```
docker-compose down
```
