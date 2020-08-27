# -*- coding: utf-8 -*-
"""
Interaction Brokers Connection

Connection Demo
"""

from IBWrapper import IBWrapper
from ib.ext.EClientSocket import EClientSocket

accountName = "DU230008"
callback = IBWrapper()        # Instantiate IBWrapper. callback 
tws = EClientSocket(callback) # Instantiate EClientSocket and return data to callback
host = "localhost"                     # For local host
port = 7497
clientId = 5

tws.eConnect(host, port, clientId) # Connect to TWS

tws.eDisconnect()
