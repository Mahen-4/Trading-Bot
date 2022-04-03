import sys
import os, sys
from botorderclient import BotOrderClient
import time

sys.path.append(os.path.join(os.path.dirname(__file__), 'Trading-Bot'))

from trade_bot import TradeBot

client = BotOrderClient()
gains = []
timestamp = []
robot = TradeBot(client)

with open("candle_sample.txt", "r") as fp:
    lines = fp.readlines()
    for line in lines:
        client.process_candle(line)
        robot.process_candle(line)
        gains += [ client.gains() ]
        timestamp += [client.last_time]

robot.plot()

print(f"Gains : {client.gains()}")
