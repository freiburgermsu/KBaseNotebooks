import sys
import os
from os import path
from zipfile import ZipFile

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from baseutil import *

import hashlib
import requests
import json
import pandas as pd
from pandas import DataFrame, read_csv, concat, set_option

class APIDemo(BaseUtil):
    def __init__(self):
        BaseUtil.__init__(self,"llm_api")
        self.msseedrecon()

util = APIDemo()