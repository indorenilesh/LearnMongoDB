#!/bin/bash
ROOT_PATH=/local/apps
MONGO_DIR=${ROOT_PATH}/mongodb
CONF_TEMP=/local/apps/tools/mongod.conf_temp

usage()
{
        echo "Usage: $0 -n <Instance Name> -p <Instance Port> ";
        echo "Your input: $0 ${@}"
        exit 1;
}
if [ $# -lt 4 ]
then
        usage
	exit
fi

while [ -n "$1" ]; do # while loop starts
    case "$1" in
    -n)
        instanceName="$2"
	instancePath=${ROOT_PATH}/${instanceName}
        shift
        ;;
    -p)
        instancePort="$2"
        shift
        ;;
    *)
        echo "Option $1 not recognized" ;;
    esac
    shift
done

mkdir ${instancePath} ${instancePath}/data ${instancePath}/logs
cp -apv ${CONF_TEMP} ${instancePath}/mongod.conf
cp -apv start.sh ${instancePath}/
cp -apv stop.sh ${instancePath}/
sed -i "s/instance_name/${instanceName}/g" ${instancePath}/mongod.conf
sed -i "s/instance_name/${instanceName}/g" ${instancePath}/start.sh
sed -i "s/instance_name/${instanceName}/g" ${instancePath}/stop.sh
sed -i "s/instance_port/${instancePort}/g" ${instancePath}/mongod.conf
