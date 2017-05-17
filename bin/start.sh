#!/bin/bash

echo "start http"

python start_server.py stop

python start_server.py start

echo "end"
