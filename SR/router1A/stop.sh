#!/bin/bash
kill -9 `ps aux |grep router1A |grep -v grep | awk '{print $2}'`
