#!/bin/bash

source config.sh

mkdir -p ${DATA_DIR}

curl_cmd='curl -s "https://api.glassnode.com/v2/metrics/endpoints?a=BTC&i=24h&f=csv&api_key='${API_KEY}'" > './endpoints_list''
eval "${curl_cmd}"

echo ""
