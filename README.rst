Kademlia 的 Python3 实现
==============================

:Date: 07/10 2017

.. contents::


介绍
--------

更改自 `https://github.com/bmuller/kademlia`  项目。


改变:


*   Python 版本切换自 Python3.5 （所有分支, 删除 Python2 代码）
*   合并 `rpcudp` 项目代码至 `kademlia` 项目
*   增强了部分代码实现


运行样例
--------

.. code:: bash
    
    # Python >= 3.5
    brew install python3
    brew upgrade python3
    
    git clone https://github.com/LuoZijun/kademlia.git
    git checkout python3.5
    
    pip3 install -r requirements.txt
    
    python3 examples/example.py
    python3 examples/get.py testkey
    python3 examples/set.py testkey testvalue


参考
--------

*   `Kademlia distributed hash table <http://en.wikipedia.org/wiki/Kademlia>`_
*   `kademlia <https://github.com/bmuller/kademlia>`_
*   `rpcudp  <https://github.com/bmuller/rpcudp>`_

