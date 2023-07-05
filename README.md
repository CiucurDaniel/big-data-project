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

Steps to run Hadoop with this setup:

```
git clone https://github.com/big-data-europe/docker-hadoop

docker-compose up -detach

docker ps
```

In order to interact with the namenode use docker exec:

```
docker exec -it namenode bash
```

From withhin the node, we can use `hdfs` commands (eg: hdfs dfs -ls ) or the main goal, run Hadoop Map Reduce Jobs.

```
# Run map reduce job from the path where you have the jar file.
hadoop jar <jar_file_name> <class_name> input output
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

## Run example world count

```
# Copy jar in namenode
docker cp .\submit\WordCount.jar e5d0addf59a1:/tmp

# Enter the namenode container
docker exec

cd /tmp 

# Run the code
$HADOOP_HOME/bin/hadoop jar WordCount.jar WordCount /input /output
```

## Course commands

```
hadoop fs -mkdir /data2
hadoop fs -ls /
```



