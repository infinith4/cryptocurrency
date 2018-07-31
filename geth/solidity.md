sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc

solc --version

which solc

# geth を起動して、コンソールに接続

nohup geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet --mine --minerthreads 1 --rpc --rpcaddr "0.0.0.0" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --unlock 0,1 --password ~/data_testnet/passwd --verbosity 6 2>> ~/data_testnet/geth.log &

~/data_testnet$ geth attach rpc:http://localhost:8545
Welcome to the Geth JavaScript console!

instance: Geth/v1.5.5-stable-ff07d548/linux/go1.6.2
coinbase: 0xedc928d2ed25180b15c023ff12dd677a76923a31
at block: 113 (Tue, 31 Jul 2018 22:04:55 JST)
 datadir: /home/th4/data_testnet
 modules: admin:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

>
"solc, the solidity compiler commandline interface\nVersion: 0.4.24+commit.e67f0147.Linux.g++\n"
>
>
["Solidity"]
