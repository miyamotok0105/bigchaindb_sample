# -*- coding: utf-8 -*-
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

bdb_root_url = 'http://0.0.0.0:9984'  # Use YOUR BigchainDB Root URL here

bdb = BigchainDB(bdb_root_url)


print(bdb.assets.get(search='abcd1234'))

