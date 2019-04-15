#!/bin/bash
kill -9 `ps aux |grep mdb1 |grep -v grep | awk '{print $2}'`
