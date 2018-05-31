# P2Pool-Config-Files
The multiple config files under networks for the daemons I am running

#### Main Dependencies:

```import os
import shutil
import sys
import zipfile
import platform

from distutils.core import setup
from distutils.sysconfig import get_python_lib
import py2exe
```
#### Required Libraries

```
sudo apt-get install build-essential g++ python-dev autotools-dev libicu-dev build-essential libbz2-dev 
sudo apt-get install libboost-all-dev
sudo apt-get install aptitude
aptitude search boost
```
### General backups of some of the network configuration files I use on P2Pool for solo-mining.

#### Make sure to use different instance for Dash, and port numbers, but try integrating same IP
