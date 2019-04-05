#!/bin/bash
kill -9 `ps aux |grep config1B |grep -v grep | awk '{print $2}'`
