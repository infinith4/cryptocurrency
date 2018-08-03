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



cat HelloWorldOrg.sol | tr -d '\n' > HelloWorld.sol
cat HelloWorld.sol
geth attach rpc:http://localhost:8545
source='pragma solidity ^0.4.8;contract HelloWorld {  string public greeting;  function HelloWorld(string _greeting) {    greeting = _greeting;  }  function setGreeting(string _greeting) {    greeting = _greeting;  }  function say() constant returns (string) {    return greeting;  }}'
sourceCompiled = eth.compile.solidity(source)

solc --abi --bin HelloWorld.solc

~/gitrepo/github/cryptocurrency/geth$ solc --abi --bin HelloWorldOrg.solc
HelloWorldOrg.solc:4:3: Warning: Defining constructors as functions with the same name as the contract is deprecated. Use "constructor(...) { ... }" instead.
  function HelloWorld(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:4:3: Warning: No visibility specified. Defaulting to "public".
  function HelloWorld(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:8:3: Warning: No visibility specified. Defaulting to "public".
  function setGreeting(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:12:3: Warning: No visibility specified. Defaulting to "public".
  function say() constant returns (string) {
  ^ (Relevant source part starts here and spans across multiple lines).

======= HelloWorldOrg.solc:HelloWorld =======
Binary:
608060405234801561001057600080fd5b50604051610514380380610514833981018060405281019080805182019291905050508060009080519060200190610049929190610050565b50506100f5565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061009157805160ff19168380011785556100bf565b828001600101855582156100bf579182015b828111156100be5782518255916020019190600101906100a3565b5b5090506100cc91906100d0565b5090565b6100f291905b808211156100ee5760008160009055506001016100d6565b5090565b90565b610410806101046000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063954ab4b21461005c578063a4136862146100ec578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100716101e5565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100b1578082015181840152602081019050610096565b50505050905090810190601f1680156100de5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156100f857600080fd5b50610153600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610287565b005b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561027d5780601f106102525761010080835404028352916020019161027d565b820191906000526020600020905b81548152906001019060200180831161026057829003601f168201915b5050505050905090565b806000908051906020019061029d92919061033f565b5050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a72305820b92e9e2b821f3bf5b10522c302cc14cc418fac6c0bda1d42b80db16dd00a08b40029
Contract JSON ABI
[{"constant":true,"inputs":[],"name":"say","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]


nohup geth --networkid 4649 --nodiscover --maxpeers 0 --datadir ~/data_testnet --mine --minerthreads 1 --rpc --rpcaddr "0.0.0.0" --rpcport 8545 --rpccorsdomain "*" --rpcapi "admin,db,eth,debug,miner,net,shh,txpool,personal,web3" --unlock 0,1 --password ~/data_testnet/passwd --verbosity 6 2>> ~/data_testnet/geth.log &

geth attach rpc:http://localhost:8545


var bin = "608060405234801561001057600080fd5b50604051610514380380610514833981018060405281019080805182019291905050508060009080519060200190610049929190610050565b50506100f5565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061009157805160ff19168380011785556100bf565b828001600101855582156100bf579182015b828111156100be5782518255916020019190600101906100a3565b5b5090506100cc91906100d0565b5090565b6100f291905b808211156100ee5760008160009055506001016100d6565b5090565b90565b610410806101046000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063954ab4b21461005c578063a4136862146100ec578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100716101e5565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100b1578082015181840152602081019050610096565b50505050905090810190601f1680156100de5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156100f857600080fd5b50610153600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610287565b005b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561027d5780601f106102525761010080835404028352916020019161027d565b820191906000526020600020905b81548152906001019060200180831161026057829003601f168201915b5050505050905090565b806000908051906020019061029d92919061033f565b5050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a72305820b92e9e2b821f3bf5b10522c302cc14cc418fac6c0bda1d42b80db16dd00a08b40029"

var abi = [{"constant":true,"inputs":[],"name":"say","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]

var contract = eth.contract(abi)

> contract.abi
[{
    constant: true,
    inputs: [],
    name: "say",
    outputs: [{
        name: "",
        type: "string"
    }],
    payable: false,
    stateMutability: "view",
    type: "function"
}, {
    constant: false,
    inputs: [{
        name: "_greeting",
        type: "string"
    }],
    name: "setGreeting",
    outputs: [],
    payable: false,
    stateMutability: "nonpayable",
    type: "function"
}, {
    constant: true,
    inputs: [],
    name: "greeting",
    outputs: [{
        name: "",
        type: "string"
    }],
    payable: false,
    stateMutability: "view",
    type: "function"
}, {
    inputs: [{
        name: "_greeting",
        type: "string"
    }],
    payable: false,
    stateMutability: "nonpayable",
    type: "constructor"
}]

> eth.contract(contract.abi)
{
  abi: [{
      constant: true,
      inputs: [],
      name: "say",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      constant: false,
      inputs: [{...}],
      name: "setGreeting",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "greeting",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      inputs: [{...}],
      payable: false,
      stateMutability: "nonpayable",
      type: "constructor"
  }],
  eth: {
    accounts: ["0xedc928d2ed25180b15c023ff12dd677a76923a31", "0x84f5c6ce6886bb8d936f2ba0cfe386ad7fc36eae"],
    blockNumber: 3026,
    coinbase: "0xedc928d2ed25180b15c023ff12dd677a76923a31",
    compile: {
      lll: function(),
      serpent: function(),
      solidity: function()
    },
    defaultAccount: undefined,
    defaultBlock: "latest",
    gasPrice: 20000000000,
    hashrate: 146278,
    mining: true,
    pendingTransactions: [],
    syncing: false,
    call: function(),
    contract: function(abi),
    estimateGas: function(),
    filter: function(fil, callback),
    getAccounts: function(callback),
    getBalance: function(),
    getBlock: function(),
    getBlockNumber: function(callback),
    getBlockTransactionCount: function(),
    getBlockUncleCount: function(),
    getCode: function(),
    getCoinbase: function(callback),
    getCompilers: function(),
    getGasPrice: function(callback),
    getHashrate: function(callback),
    getMining: function(callback),
    getNatSpec: function(),
    getPendingTransactions: function(callback),
    getRawTransaction: function(),
    getRawTransactionFromBlock: function(),
    getStorageAt: function(),
    getSyncing: function(callback),
    getTransaction: function(),
    getTransactionCount: function(),
    getTransactionFromBlock: function(),
    getTransactionReceipt: function(),
    getUncle: function(),
    getWork: function(),
    iban: function(iban),
    icapNamereg: function(),
    isSyncing: function(callback),
    namereg: function(),
    resend: function(),
    sendIBANTransaction: function(),
    sendRawTransaction: function(),
    sendTransaction: function(),
    sign: function(),
    signTransaction: function(),
    submitTransaction: function(),
    submitWork: function()
  },
  at: function(address, callback),
  getData: function(),
  new: function()
}

> sourceCompliedContract = eth.contract(contract.abi)

> _greeting = "Hello World!"
"Hello World!"

> contract = sourceCompliedContract.new(_greeting, { from: eth.accounts[0], data: bin, gas: '4700000'})
{
  abi: [{
      constant: true,
      inputs: [],
      name: "say",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      constant: false,
      inputs: [{...}],
      name: "setGreeting",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "greeting",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      inputs: [{...}],
      payable: false,
      stateMutability: "nonpayable",
      type: "constructor"
  }],
  address: undefined,
  transactionHash: "0xe2ac7e635be821f9d4ea435164b92ed70c99eaf95eb1d42982aa3e2f0b8ee7ef"
}
> contract

{
  abi: [{
      constant: true,
      inputs: [],
      name: "say",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      constant: false,
      inputs: [{...}],
      name: "setGreeting",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "greeting",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      inputs: [{...}],
      payable: false,
      stateMutability: "nonpayable",
      type: "constructor"
  }],
  address: undefined,
  transactionHash: "0xe2ac7e635be821f9d4ea435164b92ed70c99eaf95eb1d42982aa3e2f0b8ee7ef"
}
> contract
{
  abi: [{
      constant: true,
      inputs: [],
      name: "say",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      constant: false,
      inputs: [{...}],
      name: "setGreeting",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "greeting",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      inputs: [{...}],
      payable: false,
      stateMutability: "nonpayable",
      type: "constructor"
  }],
  address: "0x07f0370b226d01bdce31fe4024faa64f78a3396f",
  transactionHash: "0xe2ac7e635be821f9d4ea435164b92ed70c99eaf95eb1d42982aa3e2f0b8ee7ef",
  allEvents: function(),
  greeting: function(),
  say: function(),
  setGreeting: function()
}
> contract.say.call()

"Hello World!"
>

> contract.greeting.call()
"Hello World!"

# "Hello World!" to "Hello, Ethereum!"

> contract.setGreeting.sendTransaction("Hello, Ethereum!", {from:eth.accounts[0], gas:1000000})
"0xb019299457eb3326ca11d7262b251fe5ec6d3a9fcc45170d941682db0ca1e593"

> contract.say.call()
"Hello, Ethereum!"


# 既存のコンストラクトにアクセスする

> exit

~/gitrepo/github/cryptocurrency/geth$ solc --abi --bin HelloWorldOrg.solc
HelloWorldOrg.solc:4:3: Warning: Defining constructors as functions with the same name as the contract is deprecated. Use "constructor(...) { ... }" instead.
  function HelloWorld(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:4:3: Warning: No visibility specified. Defaulting to "public".
  function HelloWorld(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:8:3: Warning: No visibility specified. Defaulting to "public".
  function setGreeting(string _greeting) {
  ^ (Relevant source part starts here and spans across multiple lines).
HelloWorldOrg.solc:12:3: Warning: No visibility specified. Defaulting to "public".
  function say() constant returns (string) {
  ^ (Relevant source part starts here and spans across multiple lines).

======= HelloWorldOrg.solc:HelloWorld =======
Binary:
608060405234801561001057600080fd5b50604051610514380380610514833981018060405281019080805182019291905050508060009080519060200190610049929190610050565b50506100f5565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061009157805160ff19168380011785556100bf565b828001600101855582156100bf579182015b828111156100be5782518255916020019190600101906100a3565b5b5090506100cc91906100d0565b5090565b6100f291905b808211156100ee5760008160009055506001016100d6565b5090565b90565b610410806101046000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063954ab4b21461005c578063a4136862146100ec578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100716101e5565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100b1578082015181840152602081019050610096565b50505050905090810190601f1680156100de5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156100f857600080fd5b50610153600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610287565b005b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561027d5780601f106102525761010080835404028352916020019161027d565b820191906000526020600020905b81548152906001019060200180831161026057829003601f168201915b5050505050905090565b806000908051906020019061029d92919061033f565b5050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a72305820b92e9e2b821f3bf5b10522c302cc14cc418fac6c0bda1d42b80db16dd00a08b40029
Contract JSON ABI
[{"constant":true,"inputs":[],"name":"say","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]



$ geth attach rpc:http://localhost:8545

> var bin = "608060405234801561001057600080fd5b50604051610514380380610514833981018060405281019080805182019291905050508060009080519060200190610049929190610050565b50506100f5565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061009157805160ff19168380011785556100bf565b828001600101855582156100bf579182015b828111156100be5782518255916020019190600101906100a3565b5b5090506100cc91906100d0565b5090565b6100f291905b808211156100ee5760008160009055506001016100d6565b5090565b90565b610410806101046000396000f300608060405260043610610057576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168063954ab4b21461005c578063a4136862146100ec578063ef690cc014610155575b600080fd5b34801561006857600080fd5b506100716101e5565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156100b1578082015181840152602081019050610096565b50505050905090810190601f1680156100de5780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b3480156100f857600080fd5b50610153600480360381019080803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509192919290505050610287565b005b34801561016157600080fd5b5061016a6102a1565b6040518080602001828103825283818151815260200191508051906020019080838360005b838110156101aa57808201518184015260208101905061018f565b50505050905090810190601f1680156101d75780820380516001836020036101000a031916815260200191505b509250505060405180910390f35b606060008054600181600116156101000203166002900480601f01602080910402602001604051908101604052809291908181526020018280546001816001161561010002031660029004801561027d5780601f106102525761010080835404028352916020019161027d565b820191906000526020600020905b81548152906001019060200180831161026057829003601f168201915b5050505050905090565b806000908051906020019061029d92919061033f565b5050565b60008054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156103375780601f1061030c57610100808354040283529160200191610337565b820191906000526020600020905b81548152906001019060200180831161031a57829003601f168201915b505050505081565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f1061038057805160ff19168380011785556103ae565b828001600101855582156103ae579182015b828111156103ad578251825591602001919060010190610392565b5b5090506103bb91906103bf565b5090565b6103e191905b808211156103dd5760008160009055506001016103c5565b5090565b905600a165627a7a72305820b92e9e2b821f3bf5b10522c302cc14cc418fac6c0bda1d42b80db16dd00a08b40029"

var abi = [{"constant":true,"inputs":[],"name":"say","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[{"name":"_greeting","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]

var contract = eth.contract(abi)

var contractAbiDefinition = contract.abi

> contract = eth.contract(contractAbiDefinition).at("0x07f0370b226d01bdce31fe4024faa64f78a3396f")
{
  abi: [{
      constant: true,
      inputs: [],
      name: "say",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      constant: false,
      inputs: [{...}],
      name: "setGreeting",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "greeting",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }, {
      inputs: [{...}],
      payable: false,
      stateMutability: "nonpayable",
      type: "constructor"
  }],
  address: "0x07f0370b226d01bdce31fe4024faa64f78a3396f",
  transactionHash: null,
  allEvents: function(),
  greeting: function(),
  say: function(),
  setGreeting: function()
}
> contract.say.call()
"Hello, Ethereum!"
