# Run app using docker steps

### Initialize all containers
```
docker-compose up
```

### Delete all containers
```
docker-compose down
```

###### Add --rmi all to delete all images too

### Build or rebuild of image
```
docker build -t fastapi-app .
```

### Specific run the app image
```
docker run -d -p 8000:8000 --name fastapi-container fastapi-app
```
###### docker stop fastapi-container
###### docker rm fastapi-app