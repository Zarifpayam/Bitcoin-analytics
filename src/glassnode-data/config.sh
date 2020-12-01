# This is the config file for the crypto data fetcher (Glassnode API)

API_KEY_FILE="/tmp/glassnode_api_key"
API_KEY="$(cat "${API_KEY_FILE}")"
DATA_DIR="./data"
DOWNLOAD_DIR="./downloads"
GLASSNODE_HOST="https://api.glassnode.com"

ENDPOINTS_LIST_FILE="endpoints_list"
