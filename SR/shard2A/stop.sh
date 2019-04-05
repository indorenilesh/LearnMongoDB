#!/bin/bash
kill -9 `ps aux |grep shard2A |grep -v grep | awk '{print $2}'`
