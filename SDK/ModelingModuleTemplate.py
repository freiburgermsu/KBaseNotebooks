from __future__ import absolute_import

import os
import sys
import uuid
import logging
import json
import jinja2
import pandas as pd
from kbbasemodules.basemodelingmodule import BaseModelingModule

logger = logging.getLogger(__name__)

class ${module}(BaseModelingModule):
    def __init__(self,config,module_dir="/kb/module",working_dir=None,token=None,clients={},callback=None):
        BaseModelingModule.__init__(self,"${module}",config,module_dir,working_dir,token,clients,callback)
        self.version = "0.1.1.msr"
        self.module_dir = module_dir
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        
${module_functions}            
    def build_dataframe_report(self,table):        
        context = {}
        env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.module_dir+"/data/"),
            autoescape=jinja2.select_autoescape(['html', 'xml']))
        html = env.get_template("ReportTemplate.html").render(context)
        os.makedirs(self.working_dir+"/html", exist_ok=True)
        with open(self.working_dir+"/html/index.html", 'w') as f:
            f.write(html)
        #Creating data table file
        json_str = '{"data":'+table.to_json(orient='records')+'}'
        with open(self.working_dir+"/html/data.json", 'w') as f:
            f.write(json_str)