# This is the config file for the crypto data fetcher (Glassnode API)

API_KEY=""
OUTPUT_DIR="../../data"
DOWNLOAD_DIR="./downloads"

endpoints_list="/v1/metrics/transactions/count
/v1/metrics/indicators/stock_to_flow_deflection
/v1/metrics/entities/sending_count
/v1/metrics/indicators/reserve_risk
/v1/metrics/indicators/unrealized_profit
/v1/metrics/indicators/unrealized_loss
/v1/metrics/entities/receiving_count
/v1/metrics/indicators/puell_multiple
/v1/metrics/market/price_usd_close
/v1/metrics/blockchain/utxo_profit_relative
/v1/metrics/market/mvrv
/v1/metrics/transactions/transfers_volume_miners_to_exchanges
/v1/metrics/market/mvrv_more_155
/v1/metrics/transactions/transfers_volume_exchanges_net
/v1/metrics/fees/fee_ratio_multiple
/v1/metrics/distribution/balance_exchanges
/v1/metrics/indicators/unrealized_profit_account_based
/v1/metrics/entities/net_growth_count
/v1/metrics/blockchain/block_size_mean
/v1/metrics/blockchain/block_interval_mean
/v1/metrics/indicators/cdd_supply_adjusted_binary
/v1/metrics/indicators/asol
/v1/metrics/addresses/min_100_count
/v1/metrics/entities/active_count
/v1/metrics/addresses/accumulation_balance"

