## 3.0 Deploying an app using compose 
This portion of the tutorial will guide you through the creation and customization of a voting app. It's important that you follow the steps in order, and make sure to customize the portions that are customizable.

**Important.**
To complete this section, you will need to have Docker installed on your machine as mentioned in the [Setup](./setup.md) section. You'll also need to have git installed. There are many options for installing it. For instance, you can get it from [GitHub](https://help.github.com/articles/set-up-git/).

### Voting app
For this application we will use the Docker Example Voting App. This app consists of five components:


![Architecture diagram](../../example-voting-app/architecture.excalidraw.png)

* Python webapp which lets you vote between two options
* Redis queue which collects new votes
* .NET worker which consumes votes and stores them in…
* Postgres database backed by a Docker volume
* Node.js webapp which shows the results of the voting in real time

`cd` into the directory:

```
cd docker/example-voting-app
```

### 3.1 Deploying the app
For this first stage, we will use existing images that are in Docker Store.

You will need a [Docker Compose](https://docs.docker.com/compose) file. You don't need Docker Compose installed, though if you are using Docker for Mac or Docker for Windows you have it installed.

```
version: "3"
services:

  redis:
    image: redis:alpine
    ports:
      - "6379"
    networks:
      - frontend
  db:
    image: postgres:9.4
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
  vote:
    image: dockersamples/examplevotingapp_vote:before
    ports:
      - 5000:80
    networks:
      - frontend
    depends_on:
      - redis
  result:
    image: dockersamples/examplevotingapp_result:before
    ports:
      - 5001:80
    networks:
      - backend
    depends_on:
      - db

  worker:
    image: dockersamples/examplevotingapp_worker
    networks:
      - frontend
      - backend

  visualizer:
    image: dockersamples/visualizer
    ports:
      - "8080:8080"
    stop_grace_period: 1m30s
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock

networks:
  frontend:
  backend:

volumes:
  db-data:
```

First deploy it, and then we will look more deeply into the details:

```
docker compose up --detach

 ✔ Container example-voting-app-redis-1   Healthy  0.0s 
 ✔ Container example-voting-app-db-1      Healthy  0.0s 
 ✔ Container example-voting-app-vote-1    Started  0.0s 
 ✔ Container example-voting-app-worker-1  Started  0.0s 
 ✔ Container example-voting-app-result-1  Started  0.0s   
```
to verify your stack has deployed, use `docker compose ls`
```
docker compose ls
NAME                 STATUS              CONFIG FILES
example-voting-app   running(5)          docker/example-voting-app/docker-compose.yml
```

If you take a look at `docker-stack.yml`, you will see that the file defines

* vote container based on a Python image
* result container based on a Node.js image
* redis container based on a redis image, to temporarily store the data.
* .NET based worker app based on a .NET image
* Postgres container based on a postgres image

The Compose file also defines two networks, front-tier and back-tier. Each container is placed on one or two networks. Once on those networks, they can access other services on that network in code just by using the name of the service. Services can be on any number of networks. Services are isolated on their network. Services are only able to discover each other by name if they are on the same network.

Take a look at the file again. You'll see it starts with

```
version: "3"
```


The `image` key there specifies which image you can use, in this case the image `dockersamples/examplevotingapp_vote:before`. If you're familiar with Compose, you may know that there's a `build` key, which builds based on a Dockerfile.

Much like `docker run` you will see you can define `ports` and `networks`. There's also a `depends_on` key which allows you to specify that a service is only deployed after another service, in this case `vote` only deploys after `redis`.

You can specify other properties, like when to restart, what [healthcheck](https://docs.docker.com/engine/reference/builder/#healthcheck) to use, placement constraints, resources, etc.

#### Test run

Now that the app is running, you can go to `http://localhost:5000` to see:

<img src="../images/vote.png" title="vote">

Click on one to vote. You can check the results at `http://localhost:5001`.

#### 3.2 Remove the compose

Remove the compose

```
docker compose down
```

### 3.3 Next steps
Now that you've built some images and pushed them to Docker Cloud, and learned the basics of Swarm mode, you can explore more of Docker by checking out [the documentation](https://docs.docker.com). And if you need any help, check out the [Docker Forums](https://forums.docker.com) or [StackOverflow](https://stackoverflow.com/tags/docker/).

## Exercises
1. Add healthcheck for voting service that will run `curl http://localhost` every 15s with timeout equal to 5s and start_period 10s
