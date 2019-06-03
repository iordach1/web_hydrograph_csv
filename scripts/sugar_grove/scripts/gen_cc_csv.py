# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:27:05 2019

@author: iordach1

generates a "carbon copy" .csv of .dat files for Green River Lowlands telemetry wells

modified waterLevel/water_Level field to be more explicit to aquifer in nested situations

task scheduled to run every hour on the 10's from SWSIWIPCOORD

script takes ~30 seconds to run to completion

--TO DO--
modify to append to an existing file... to account for data loss in future
"""

from GRL_well_objects import GRL_well_dictionary

for key, obj in GRL_well_dictionary.items():    obj.gen_cc_csv()

#print("done")