# Showtime

## Client
### Commands to get you started
- Build: 
```
./gradlew androidDependencies
```

- Run unit tests: 
```
./gradlew lint test
```

## Backend
### Commands to get you started
- Build and deploy: 
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

- Migrate DB: 
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml run server python3 manage.py makemigrations app
```

- Run unit tests: 
```
docker-compose -f docker-compose.yml -f docker-compose.dev.yml run server python3 manage.py test
```

**Note**: `docker-compose.dev.yml` define docker volumes that makes life easier to developers. If you don't want to use volumes deploy using only the file `docker-compose.yml`. E.g. `docker-compose up`
