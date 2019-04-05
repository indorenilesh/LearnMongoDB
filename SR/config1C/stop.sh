#!/bin/bash
kill -9 `ps aux |grep config1C |grep -v grep | awk '{print $2}'`
