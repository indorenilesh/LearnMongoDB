#!/bin/bash
kill -9 `ps aux |grep mdb3 |grep -v grep | awk '{print $2}'`
