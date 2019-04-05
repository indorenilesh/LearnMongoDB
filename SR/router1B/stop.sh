#!/bin/bash
kill -9 `ps aux |grep router1B |grep -v grep | awk '{print $2}'`
