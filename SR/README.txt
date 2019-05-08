1) This SR setup have below servers.
    3 shard + replication servers
    3 config + replication servers
    3 mongos + replication servers.

2) How to start SR setup.
    1) Start all config servers.
        config1A/start.sh
        config1B/start.sh
        config1C/start.sh
    2)  Start all shard servers.
        shard1A/start.sh
        shard1B/start.sh
        shard1C/start.sh
        shard2A/start.sh
        shard2B/start.sh
        shard2C/start.sh
    3)  Start all Mongos servers.
        router1A/start.sh
        router1B/start.sh
        router1C/start.sh

3) How to stop SR setup.
    1) Stop all mongos servers.
        router1A.stop/stop.sh
        router1B/stop.sh
        router1C/stop.sh
    2) Stop all shard servers.
        shard1A/stop.sh
        shard1B/stop.sh
        shard1C/stop.sh
        shard2A/stop.sh
        shard2B/stop.sh
        shard2C/stop.sh
    3) Stop all config servers.
        config1A/stop.sh
        config1B/stop.sh
        config1C/stop.sh





Restore/Push data in SR setup.
mongorestore -d stock -c tick_data --port 27041 tick_data/stock/tick_data.bson