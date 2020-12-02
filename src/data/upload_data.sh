#!/bin/bash

source config.sh

aws s3 sync output/ s3://glassnode-data/
