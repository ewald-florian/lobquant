
import pandas as pd
import lobquant as lq

# Load own data
trade_data = pd.read_csv('trades.csv')
lob_data = pd.read_csv('lob.csv')

# lob_data should have som form of Leve-Columns including price quantity and 
# opitonally number of orders and a timestamp column

# trade_data should include columns for timestamp, price, quantity and optionally side and other information

tq_trades = tq.trades(data='trades.csv',
                      price_col='price',
                      quantity_col='quantity',
                      side_col='side',
                      aggressor_buy='buy',
                      aggressor_sell='sell')

# TODO: Find a simple and general way to parse column names!
# TODO: Find a simple and general way to deal with the target frequency (e.g. for every measure separately or for the entire df...)
tq_lob = tq.lob(data='lob.csv',
                column_name_style='...',
                target_frequency='...'
                )

# Examples to compute singular measures
spread_1m = tq_lob.spread(freq='1m', averaging='twa')

depth_10_daily = tq_lob.depthx(x=10, freq='1D', averaging='twa')


# Example to process entire dfs:
processed_trades_daily = tq_trades(measures=['volume', 'notional', 'realized_vola'], freq='1D')

processed_lob_daily = tq_lob(measures=['spread', 'depth10', 'oib'], freq='1D', averaging='twa')


# Improvements:

# Use classes for LobData and TradeDate
from lobquant import LobData, TradeData

lob = LobData(data='lob.csv', price_col_map='your_format')  # price_col_map could refer to a built-in parser
spread = lob.spread(freq='1min')

trades = TradeData(data='trades.csv', price_col='price', quantity_col='qty', side_col='side')
summary = trades(measures=['volume'], freq='1D')

# Column Name mapping and autodetection:
# One way would be to use dictionaries
tq_trades = TradeData('trades.csv', column_map={'timestamp': 'ts', 'price': 'p'})
# OR
tq_trades = TradeData('trades.csv', column_name_style='lobster')

# Use a built in example dataset
from lobquant.datasets import load_sample_lob, load_sample_trades

lob_df = load_sample_lob()
trades_df = load_sample_trades()

# Maybe use existing lob styles like lobster (Mannheim) or ITCH (Nasdaq)




