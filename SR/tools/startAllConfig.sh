#!/bin/bash
ROOT_DIR=/local/apps/SR/
LIST=`ls ${ROOT_DIR} |grep ^config`
for i in ${LIST}
do
        cd ${ROOT_DIR}/$i
        ./start.sh
done