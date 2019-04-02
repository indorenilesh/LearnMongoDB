#!/bin/bash
kill -9 `ps aux |grep instance_name |grep -v grep | awk '{print $2}'`
