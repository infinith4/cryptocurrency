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
eth.accounts[1]

exit

$ geth --datadir ~/data_testnet account new
Your new account is locked with a password. Please give a password. Do not forget this password.
Passphrase:
Repeat passphrase:
Address: {eb3fbed5f607625056b73436b7174f8c3a54659b}

$ geth --datadir ~/data_testnet account list
Account #0: {537d6770ad5510cb1d1b0ce776a803fa5359ff8b} /home/th4/data_testnet/keystore/UTC--2018-07-19T13-54-08.281288704Z--537d6770ad5510cb1d1b0ce776a803fa5359ff8b
Account #1: {3bb960dadd4c966a4e25d6937e4c09af0cb14a86} /home/th4/data_testnet/keystore/UTC--2018-07-19T13-54-22.211602272Z--3bb960dadd4c966a4e25d6937e4c09af0cb14a86
Account #2: {eb3fbed5f607625056b73436b7174f8c3a54659b} /home/th4/data_testnet/keystore/UTC--2018-07-21T15-46-17.498666690Z--eb3fbed5f607625056b73436b7174f8c3a54659b


# mining

geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet console 2>> ~/data_testnet/geth.log

> eth.coinbase
"0x537d6770ad5510cb1d1b0ce776a803fa5359ff8b"
> miner.setEtherbase(eth.accounts[1])
true
> eth.coinbase
"0x3bb960dadd4c966a4e25d6937e4c09af0cb14a86"
> miner.setEtherbase(eth.accounts[0])
true
> eth.coinbase
"0x537d6770ad5510cb1d1b0ce776a803fa5359ff8b"
> eth.getBalance(eth.accounts[0])
0
> eth.getBalance(eth.accounts[1])
0
> eth.getBalance(eth.accounts[2])
0
> eth.blockNumber
0
