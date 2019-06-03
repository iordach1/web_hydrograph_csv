# -*- coding: utf-8 -*-
"""
Created on Tue May 21 11:34:04 2019

@author: iordach1
"""

from GRL_well_objects import GRL_well_dictionary
from warnings import filterwarnings; filterwarnings('ignore')

for key, obj in GRL_well_dictionary.items():    obj.gen_mpl_hydrograph()