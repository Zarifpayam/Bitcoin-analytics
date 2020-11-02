#!/bin/bash

source config.sh

aws s3 sync $DATA_DIR s3://glassnode-data/
