sudo add-apt-repository ppa:ethereum/ethereum
sudo apt-get update
sudo apt-get install solc

solc --version

which solc

# geth を起動して、コンソールに接続

nohup geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet --mine --minerthreads 1 --rpc --rpcaddr "0.0.0.0" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --unlock 0,1 --password ~/data_testnet/passwd --verbosity 6 2>> ~/data_testnet/geth.log &

geth attach rpc:http://localhost:8545
