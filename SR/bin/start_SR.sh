#!/bin/bash
ROOT_DIR="/local/apps/SR"
SHARD_SERVERS="shard1A shard1B shard1C shard2A shard2B shard2C"
CONFIG_SERVERS="config1A config1B config1C"
MONGOS_SERVERS="router1A router1B router1C"

#Start config servers
for i in $CONFIG_SERVERS
do
    ${ROOT_DIR}/$i/start.sh
    sleep 5
done

#Start shard servers
for i in $SHARD_SERVERS
do
    ${ROOT_DIR}/$i/start.sh
    sleep 5
done

#Start Mongos servers
for i in $MONGOS_SERVERS
do
    ${ROOT_DIR}/$i/start.sh
    sleep 5
done