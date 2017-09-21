from File.FileManager import FileManager
from Trade.TradeProcessor import TradeProcessor

# gather csv data
trade_provider = FileManager()
trade_processor = TradeProcessor(trade_provider)

# process trade information into a grouped, 2d sorted list
processed_trades = trade_processor.process_trades()

# output csv data
trade_provider.save_trades(processed_trades)
