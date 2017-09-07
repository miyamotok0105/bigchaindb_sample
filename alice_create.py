# -*- coding: utf-8 -*-
from bigchaindb_driver import BigchainDB
from bigchaindb_driver.crypto import generate_keypair
from time import sleep
from sys import exit

alice_private_key = "DPPyXUWoGTYHogj13DQH7jkPJsZSteFGM8e5rU8M8p6k"
alice_public_key = "J6uQApohNhMnsnYx4r8BKiEtyRu7GFEW5z5WgghMk15a"

bdb_root_url = 'http://0.0.0.0:9984'  # Use YOUR BigchainDB Root URL here

bdb = BigchainDB(bdb_root_url)


bdb.assets.get(search='bigchaindb')


creation_tx = bdb.transactions.retrieve(txid)

bicycle_asset = {
    'data': {
        'bicycle': {
            'serial_number': 'aaaaaa',
            'manufacturer': 'bbbbb'
        },
    },
}

bicycle_asset_metadata = {
    'planet': 'earth'
}

#Assetクリエーション
prepared_creation_tx = bdb.transactions.prepare(
    operation='CREATE',
    signers=alice.public_key,
    asset=bicycle_asset,
    metadata=bicycle_asset_metadata
)

#トランザクションは、Aliceの秘密鍵で署名することで実現する必要があります。
fulfilled_creation_tx = bdb.transactions.fulfill(
    prepared_creation_tx,
    private_keys=alice.private_key
)

sent_creation_tx = bdb.transactions.send(fulfilled_creation_tx)

txid = fulfilled_creation_tx['id']

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

