# coding=utf-8

import sys
# ............python2......python3
import ssl
from Baidu import Baidu

if __name__ == "__main__":
    ssl._create_default_https_context = ssl._create_unverified_context
    baidu = Baidu()
    baidu.plant_identification()