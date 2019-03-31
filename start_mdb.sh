#!/bin/bash
for i in `ls /local/apps |grep ^mdb`
do
/local/apps/$i/start.sh
done
