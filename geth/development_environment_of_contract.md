# install Browser-Solidity

available https://github.com/ethereum/remix-ide

$ git clone https://github.com/ethereum/remix-ide.git

## origin/gh-pages is always the latest stable build of Remix.

$ git checkout origin/gh-pages


# 既存のコンストラクトにアクセスする

address is 0x07f0370b226d01bdce31fe4024faa64f78a3396f


# send coin

```
pragma solidity ^0.4.8;

contract RecvEther {
    address public sender;  //送信者アドレス確認用の変数
    uint public recvEther;  //受け付けたEther（合計）
    function () payable {
        sender = msg.sender;  //確認のため、状態変数を更新
        recvEther += msg.value;
    }
}
```

> eth.getBalance("0xedc928d2ed25180b15c023ff12dd677a76923a31")

2.0509999999999999999998e+22
> web3.fromWei(eth.getBalance("0xedc928d2ed25180b15c023ff12dd677a76923a31"), "ether")
20509.999999999999999998

> eth.getBalance("0x84f5c6ce6886bb8d936f2ba0cfe386ad7fc36eae")

8999368460000000000
> web3.fromWei(eth.getBalance("0x84f5c6ce6886bb8d936f2ba0cfe386ad7fc36eae"), "ether")

8.99936846


## develop contract

```
pragma solidity ^0.4.8;

contract DataTypeSample {
  function getValueType() constant returns (uint) {
    uint a;
    a = 1;
    uint b = a;
    b = 2;
    return a;
  }

  function getReferenceType() constant returns (uint[2]) {
    uint[2] a;
    a[0] = 1;
    a[1] = 2;
    uint[2] b = a;
    b[0] = 10;
    b[1] = 20;
    return a;
  }
}
```

```
pragma solidity ^0.4.8;

contract IntSample {
  function division() constant returns (uint) {
    uint a = 3;
    uint b = 2;
    uint c = a / b * 10;
    return c;
  }

  function divisionLiterals() constant returns (uint) {
    uint c = 3 / 2 * 10;
    return c;
  }

  function shift() constant returns (uint[2]){
    uint[2] a;
    a[0] = 16 << 2;
    a[1] = 16 >> 2;
    return a;
  }
}
```


```
pragma solidity ^0.4.8;

contract AddressSample {
  function () payable {}
    function getBalance(address _target) constant returns (uint){
      if(_target == address(0)){
        _target = this;
      }
      return _target.balance;
    }
}
```
