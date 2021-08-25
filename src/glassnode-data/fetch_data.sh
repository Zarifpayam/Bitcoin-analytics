#!/bin/bash

source config.sh

ep_category_filter=""

mkdir -p ${DATA_DIR}
ENDPOINTS_LIST="$(cat "${ENDPOINTS_LIST_FILE}")"
ep_len="$(echo "${ENDPOINTS_LIST}" | jq -r 'length')"
ep_max="$(echo "${ENDPOINTS_LIST}" | jq -r 'length - 1')"
until=""
echo "Downloading $ep_len metrics from Glassnode ..."

count=0

json_metrics="transfers_volume_miners_to_exchanges_all balance_exchanges_all balance_miners_all supply_distribution_relative"
format="csv"

for ep_index in $( seq 0 $ep_max ); do
	echo "==================================================================================================================="
        ep_tier="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].tier')"
        echo $ep_tier
        [ $ep_tier -ne 1 ] && continue
	ep_path="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].path')"
	ep_category="$(echo "$ep_path" | awk -F'/' '{print $4}')"
	ep_name="$(echo "$ep_path" | awk -F'metrics/' '{print $2}')"
        ep_metric="$(echo $ep_name | awk -F/ '{print $2}')"
	ep_symbol="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].symbol')"
	ep_res_list="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].resolutions[]')"
	ep_assets="$(echo "${ENDPOINTS_LIST}" | jq -r '.['${ep_index}'].assets[].symbol')"

	if [ "$(grep "$ep_metric" <<< $json_metrics )" == "" ]; then
	    format="csv"
    else
        format="json"
    fi

	# Create the category dir if it doesn't exists
	[ ! -d "${DATA_DIR}/$ep_category" ] && mkdir -p ${DATA_DIR}/$ep_category

    for asset in BTC; do

        [ "$( grep $asset <<< $ep_assets )" == "" ] && continue
        format=json
        
        for resolution in $ep_res_list; do
            [ "$resolution" != "24h" ] && continue
            echo $asset $resolution $format
            curl_cmd='curl -s "'${GLASSNODE_HOST}${ep_path}'?a=${asset}&i='${resolution}'&s=1620086400&f=${format}&api_key='${API_KEY}'" > metric.tmp'
            echo $curl_cmd
            eval "${curl_cmd}"
            res=$?

            if [ $res -ne 0 ]; then
                echo "There was an issue while fetching the data for $endpoint"
                echo "Try running this command manually:"
                echo "${curl_cmd}"
            fi

            if [ "$(cat metric.tmp | grep forbidden)" == "" ]; then
                echo "$ep_index $ep_path ${asset} $resolution > ${DATA_DIR}/${ep_name}_${asset}_${resolution}.txt"
                jq -rc '.[] | "\(.t),\(.v)"' metric.tmp > met
                cp met "${DATA_DIR}/${ep_name}_${asset}_${resolution}.txt"
#                cp metric.tmp "${DATA_DIR}/${ep_name}_${asset}_${resolution}.txt"
                ((count++))
            else
                echo "$ep_index $ep_path ${asset} $resolution: $(cat metric.tmp)"
            fi
            sleep 0.5
        done
    done
done

echo "============================================="
echo "FINISHED FETCHING THE DATA FROM GLASSNODE.COM"
echo "Number of fetched metrics: $count"
