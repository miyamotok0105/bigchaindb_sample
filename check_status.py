# -*- coding: utf-8 -*-
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

bdb_root_url = 'http://0.0.0.0:9984'  # Use YOUR BigchainDB Root URL here

bdb = BigchainDB(bdb_root_url)

txid = "1266cc9151f470aa9a41644936729d8bc52436afee07854a7719a009a317d37d"

trials = 0
while trials < 60:
    try:
        if bdb.transactions.status(txid).get('status') == 'valid':
            print('Tx valid in:', trials, 'secs')
            break
    except bigchaindb_driver.exceptions.NotFoundError:
        trials += 1
        sleep(1)

if trials == 60:
    print('Tx is still being processed... Bye!')
    exit(0)

print(txid)
