$ geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet --mine --minerthreads 1 --rpc --rpcaddr "0.0.0.0" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --unlock 0 --verbosity 6 console 2>> ~/data_testnet/geth.log
Unlocking account 0 | Attempt 1/3
Passphrase:
Welcome to the Geth JavaScript console!

instance: Geth/v1.5.5-stable-ff07d548/linux/go1.6.2
coinbase: 0x537d6770ad5510cb1d1b0ce776a803fa5359ff8b
at block: 6725 (Sun, 22 Jul 2018 15:53:51 JST)
 datadir: /home/th4/data_testnet
 modules: admin:1.0 debug:1.0 eth:1.0 miner:1.0 net:1.0 personal:1.0 rpc:1.0 txpool:1.0 web3:1.0

> web3.fromWei(eth.getBalance(eth.accounts[1]), "ether")
> eth.sendTransaction({from: eth.accounts[0], to: eth.accounts[1], value: web3.toWei(10, "ether")})
> web3.fromWei(eth.getBalance(eth.accounts[1]), "ether")

$ geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet --mine --minerthreads 1 --rpc --rpcaddr "0.0.0.0" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --unlock 0 --password ~/data_testnet/passwd --verbosity 6 console 2>> ~/data_testnet/geth.log
