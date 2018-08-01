~/gitrepo/github/cryptocurrency/geth$ solc --abi --bin ex1.solc

======= ex1.solc:SingleNumRegister =======
Binary:
608060405234801561001057600080fd5b5060df8061001f6000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820d22fa895de64954148b498bba861391d8084bdc1e7d936e1f21ed38e3766b4af0029
Contract JSON ABI
[{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get","outputs":[{"name":"retVal","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]

> var bin = "0x608060405234801561001057600080fd5b5060df8061001f6000396000f3006080604052600436106049576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff16806360fe47b114604e5780636d4ce63c146078575b600080fd5b348015605957600080fd5b5060766004803603810190808035906020019092919050505060a0565b005b348015608357600080fd5b50608a60aa565b6040518082815260200191505060405180910390f35b8060008190555050565b600080549050905600a165627a7a72305820d22fa895de64954148b498bba861391d8084bdc1e7d936e1f21ed38e3766b4af0029"
undefined
> var abi = [{"constant":false,"inputs":[{"name":"x","type":"uint256"}],"name":"set","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"get
undefined
> var contract = eth.contract(abi)
undefined
>
undefined
>
undefined
>
undefined
> var myCntract = contract.new({ from: eth.accounts[0], data: bin})
undefined
> myContract
{
  abi: [{
      constant: false,
      inputs: [{...}],
      name: "set",
      outputs: [],
      payable: false,
      stateMutability: "nonpayable",
      type: "function"
  }, {
      constant: true,
      inputs: [],
      name: "get",
      outputs: [{...}],
      payable: false,
      stateMutability: "view",
      type: "function"
  }],
  address: "0x1628ceb2f6248e75f85a759164c2e816fdbb42cb",
  transactionHash: "0x945820ee3d7b9262428b16dfe64eabe7d295b7a5c51a071df716e1a90fbedd9f",
  allEvents: function(),
  get: function(),
  set: function()
}
>
> myContract.abi
[{
    constant: false,
    inputs: [{
        name: "x",
        type: "uint256"
    }],
    name: "set",
    outputs: [],
    payable: false,
    stateMutability: "nonpayable",
    type: "function"
}, {
    constant: true,
    inputs: [],
    name: "get",
    outputs: [{
        name: "retVal",
        type: "uint256"
    }],
    payable: false,
    stateMutability: "view",
    type: "function"
}]
>
