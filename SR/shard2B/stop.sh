#!/bin/bash
kill -9 `ps aux |grep shard2B |grep -v grep | awk '{print $2}'`
