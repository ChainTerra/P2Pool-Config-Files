# P2Pool-Config-Files
The multiple config files under networks for the daemons I am running

### Main Dependencies:

```import os
import shutil
import sys
import zipfile
import platform

from distutils.core import setup
from distutils.sysconfig import get_python_lib
import py2exe
```
### Frontends
#### Dash: https://github.com/justino/p2pool-ui-punchy
#### Bitcoin: https://github.com/johndoe75/p2pool-node-status

### Required Libraries

```
sudo apt-get install build-essential g++ python-dev autotools-dev libicu-dev build-essential libbz2-dev 
sudo apt-get install libboost-all-dev
sudo apt-get install aptitude
aptitude search boost
```
### General backups of some of the network configuration files I use on P2Pool for solo-mining.

||| Use the -n command to add to peers incoming connections when running

###### Make sure whether the version of P2Pool you are running requires a bitcoind node
###### *Usually for just Dashd, a BTC node isn't needed

#### I recommend using a different instance for Dash, and port numbers, but try integrating same IP
```
./minerd --url=stratum+tcp://chain-pool.com:7903 --userpass=UserPass.workername:WorkerName
```
