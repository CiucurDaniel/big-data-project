# big-data-project

Repository which contains my project for Big Data course.

## Layout

* **algorithms** contains contains the implementations for the chosen algorithms

* **report** contains the report and the presentation.

* **docker-hadoop** Docker-compose file for running Hadoop taken from this [repository](https://github.com/big-data-europe/docker-hadoop) 

## Hadoop setup

In order to setup Hadoop I made use of the following repository: [docker-hadoop](https://github.com/big-data-europe/docker-hadoop).

Following are needed:

```
docker --version
docker-compose --version
git --version
```

### Hadoop endpoints

This setup will also give you some usefull endpoints to use while developing.

```
* Namenode: http://localhost:9870/dfshealth.html#tab-overview
* History server: http://localhost:8188/applicationhistory
* Datanode: http://localhost:9864/
* Nodemanager: http://localhost:8042/node
* Resource manager: http://localhost:8088/
```



