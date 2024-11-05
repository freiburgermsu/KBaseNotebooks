import sys
import os
from os import path
from zipfile import ZipFile

# Add the parent directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
folder_name = os.path.basename(script_dir)

from baseutil import *

import hashlib
import requests
import json
import pandas as pd
from pandas import DataFrame, read_csv, concat, set_option

class NotebookUtil(BaseUtil):
    def __init__(self):
        print(folder_name)
        BaseUtil.__init__(self,folder_name)

util = NotebookUtil()