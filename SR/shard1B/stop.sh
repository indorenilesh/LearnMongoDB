#!/bin/bash
kill -9 `ps aux |grep shard1B |grep -v grep | awk '{print $2}'`
