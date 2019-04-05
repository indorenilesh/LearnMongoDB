#!/bin/bash
kill -9 `ps aux |grep shard2C |grep -v grep | awk '{print $2}'`
