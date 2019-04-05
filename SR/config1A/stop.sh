#!/bin/bash
kill -9 `ps aux |grep config1A |grep -v grep | awk '{print $2}'`
