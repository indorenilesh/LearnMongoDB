#!/bin/bash
ROOT_DIR="/local/apps/SR/shard1B"
MONGOD_BIN=/local/apps/mongodb/bin/mongod
MONGOD_CONF=${ROOT_DIR}/mongod.conf

${MONGOD_BIN} -f ${MONGOD_CONF} 
