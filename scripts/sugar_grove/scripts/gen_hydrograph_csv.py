# -*- coding: utf-8 -*-
"""
Created on Mon May 20 16:56:44 2019

@author: iordach1
"""

from GRL_well_objects import GRL_well_dictionary
from warnings import filterwarnings; filterwarnings('ignore')

for key, obj in GRL_well_dictionary.items():    obj.gen_hydrograph_csv()