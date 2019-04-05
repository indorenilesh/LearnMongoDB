#!/bin/bash
kill -9 `ps aux |grep shard1C |grep -v grep | awk '{print $2}'`
