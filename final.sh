#!/bin/bash


CONTAINER_ID=$(docker ps -a | grep container1 | awk '{print $1}')

docker cp $CONTAINER_ID:/home/doc-bd-a1/res_dpre.csv ./bd-a1/service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/eda-in-1.txt ./bd-a1/service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/vis.png ./bd-a1/service-result/
docker cp $CONTAINER_ID:/home/doc-bd-a1/k.txt ./bd-a1/service-result/


docker stop $CONTAINER_ID