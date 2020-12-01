#!/bin/bash

source config.sh

ep_category_filter="$"

mkdir -p ${DATA_DIR}
ENDPOINTS_LIST="$(cat "${ENDPOINTS_LIST_FILE}")"
ep_len="$(echo "${ENDPOINTS_LIST}" | jq -r 'length')"
ep_max="$(echo "${ENDPOINTS_LIST}" | jq -r 'length - 1')"
echo "Downloading $ep_len metrics from Glassnode ..."

count=0

for ep_index in $( seq 0 $ep_max ); do
	echo "==================================================================================================================="
	ep_path="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].path')"
	ep_category="$(echo "$ep_path" | awk -F'/' '{print $4}')"

	#Filter based on category name
	[ "$(echo $ep_category | grep "$ep_category_filter")" == "" ] && echo "Skipping metric" && continue

	ep_name="$(echo "$ep_path" | awk -F'metrics/' '{print $2}')"

	# Set the ep_res based on ep_category
	ep_res_list="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].resolutions')"
	if [ "$(echo "$ep_category" | grep "supply")" != "" ]; then
		ep_res="24h"
	elif [ "$(echo "$ep_category" | grep "addresses")" != "" ]; then
		ep_res="24h"
	elif [ "$(echo "$ep_category" | grep "derivatives")" != "" ]; then
		ep_res="24h"
	else
		if [ "$(echo "$ep_res_list" | grep 10m)" != "" ]; then
			ep_res="10m"
		elif [ "$(echo "$ep_res_list" | grep 1h)" != "" ]; then
			ep_res="1h"
		elif [ "$(echo "$ep_res_list" | grep 24h)" != "" ]; then
			ep_res="24h"
		fi
	fi

	ep_symbols="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].symbols')"

	echo "$ep_index $ep_path $ep_res > ${DATA_DIR}/${ep_name}"

	# create the category dir if it doesn't exists
	[ ! -d "${DATA_DIR}/$ep_category" ] && mkdir -p ${DATA_DIR}/$ep_category

	curl_cmd='curl -s "'${GLASSNODE_HOST}${ep_path}'?a=BTC&i='$ep_res'&f=csv&api_key='${API_KEY}'" > '${DATA_DIR}/${ep_name}''
	eval "${curl_cmd}"
	res=$?

	if [ $res -ne 0 ]; then
		echo "There was an issue while fetching the data for $endpoint"
		echo "Try running this command manually:"
		echo "${curl_cmd}"
	fi

	((count++))
done
