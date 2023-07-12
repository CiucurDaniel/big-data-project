# Apriori using MapReduce

# Run

```bash
docker cp .\apriori\target\apriori-1.0-SNAPSHOT.jar namenode:/tmp

docker cp .\mushroom.dat namenode:/tmp

docker exec -it namenode /bin/bash

hdfs dfsadmin -safemode leave 

hadoop fs -rm -r /app-logs

hadoop fs -ls /

hadoop fs -mkdir /mushroom

hadoop fs -copyFromLocal mushroom.dat /mushroom

$HADOOP_HOME/bin/hadoop jar apriori-1.0-SNAPSHOT.jar uvt.bigdata.Main /mushroom /output 20

```