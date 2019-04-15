#!/bin/bash
ROOT_DIR="/local/apps/mdb1"
MONGOD_BIN=/local/apps/mongodb/bin/mongod
MONGOD_CONF=${ROOT_DIR}/mongod.conf

${MONGOD_BIN} -f ${MONGOD_CONF} 
