#!/bin/bash
kill -9 `ps aux |grep shard1A |grep -v grep | awk '{print $2}'`
