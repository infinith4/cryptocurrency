sudo apt-get install -y build-essential libgmp3-dev golang git tree
$ git clone https://github.com/ethereum/go-ethereum.git
cd go-ethereum
$ git checkout refs/tags/v1.5.5
make go-ethereum
./build/bin/geth version

sudo cp build/bin/geth /usr/local/bin/
which geth


mkdir ~/data_testnet
cp genesis.json ~/data_testnet
geth --datadir ~/data_testnet init ~/data_testnet/genesis.json
~/gitrepo/github/go-ethereum$ geth --datadir ~/data_testnet init ~/data_testnet/genesis.json
I0719 22:48:37.554278 cmd/utils/flags.go:615] WARNING: No etherbase set and no accounts found as default
I0719 22:48:37.554339 ethdb/database.go:83] Allotted 128MB cache and 1024 file handles to /home/th4/data_testnet/geth/chaindata
I0719 22:48:37.564396 ethdb/database.go:176] closed db:/home/th4/data_testnet/geth/chaindata
I0719 22:48:37.564448 ethdb/database.go:83] Allotted 128MB cache and 1024 file handles to /home/th4/data_testnet/geth/chaindata
I0719 22:48:37.581536 cmd/geth/chaincmd.go:131] successfully wrote genesis block and/or chain rule set: 4b7556eb256a3c9fa1539df3f660fa7326927e8f16da9270f77568956613cf12

$ tree
.
├── genesis.json
├── geth
│   └── chaindata
│       ├── 000002.log
│       ├── CURRENT
│       ├── LOCK
│       ├── LOG
│       └── MANIFEST-000003
└── keystore

3 directories, 6 files

geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet console 2>> ~/data_testnet/geth.log

personal.newAccount("pass0")

eth.accounts
eth.accounts[0]
