#!/bin/bash
ROOT_DIR="/local/apps/SR/router1A"
MONGOD_BIN=/local/apps/mongodb/bin/mongos
MONGOD_CONF=${ROOT_DIR}/mongod.conf

${MONGOD_BIN} -f ${MONGOD_CONF} 
