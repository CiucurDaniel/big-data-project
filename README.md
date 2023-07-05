# big-data-project

Repository which contains my project for Big Data course.

## Layout

* **algorithms** contains contains the implementations for the chosen algorithms

* **report** contains the report and the presentation.

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