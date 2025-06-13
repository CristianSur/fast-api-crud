# Run app using docker steps

### Initialize all containers
```
docker-compose up
```

### Delete all containers and images
```
docker-compose down --rmi all
```

###### In case you need to delete only containers don't use --rmi all

### Specific build of image (when we want to save Database)
```
docker build -t fastapi-app .
```

### Specific run the app image
```
docker run -d -p 8000:8000 --name fastapi-container fastapi-app
```
###### docker stop fastapi-container
###### docker rm fastapi-app