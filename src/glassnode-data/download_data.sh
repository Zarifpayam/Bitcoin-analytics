#!/bin/bash

source config.sh

aws s3 sync s3://glassnode-data/ ${DOWNLOAD_DIR}
