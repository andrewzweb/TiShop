# Use dockerr for deploy app 

### Build container

Docker file in deploy/Dockerfile

Up to root of project and build container

```
docker build -t ti-shop -f deploy/Dockerfile .
```

If everything done. You can run container 

### Run container 

```
docker run -p 8000:8000 -d ti-shop
```

Check what all work 

```
docker ps -a 
```

There you should see name container ti-shop. 

And after can check http://you-ip.com:8000
If run local http://localhost:8000/

### Stop and remove container 

```
docker stop [CONTAINER_NAME] && docker rm [CONTAINER_NAME]
```

If you many times run and don't remove containers you can use this command 

```
docker rm $(docker ps -aq)
```

