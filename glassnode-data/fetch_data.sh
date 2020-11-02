#!/bin/bash

source config.sh

mkdir -p ${OUTPUT_DIR}

echo "Number of metrics to fetch: $(echo "$endpoints_list" | wc -l)"

count=0

for endpoint in ${endpoints_list}; do
	echo "==================================================================================================================="
	metric_name="$(echo $endpoint | awk -F'/' '{print $NF}')"

	curl_cmd='curl -s "https://api.glassnode.com'${endpoint}'?a=BTC&i=24h&f=csv&api_key='${API_KEY}'" > '${OUTPUT_DIR}/${metric_name}''
	echo "${count}: ${metric_name} > ${OUTPUT_DIR}/${metric_name}"

	eval "${curl_cmd}"
	res=$?

	if [ $res -ne 0 ]; then
		echo "There was an issue while fetching the data for $endpoint"
		echo "Try running this command manually:"
		echo "${curl_cmd}"
	fi

	((count++))
done
