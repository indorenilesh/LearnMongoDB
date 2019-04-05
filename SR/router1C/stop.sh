#!/bin/bash
kill -9 `ps aux |grep router1C |grep -v grep | awk '{print $2}'`
