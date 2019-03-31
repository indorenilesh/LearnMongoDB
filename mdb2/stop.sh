#!/bin/bash
kill -9 `ps aux |grep mdb2 |grep -v grep | awk '{print $2}'`
