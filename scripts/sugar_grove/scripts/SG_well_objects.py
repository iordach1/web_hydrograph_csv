# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:29:43 2019

@author: iordach1
"""
import pandas as pd
from SG_well_class import SG_Well


SG_well_dictionary = {}

#AURORA MUNICIPAL AIRPORT
dat_file = "Aurora_Airport.dat"
well_name = "AURORA MUNICIPAL AIRPORT"
p_num = 65886
aquifer = "silurian dolomite"
top_of_casing = 705.04
stick_up = 1.38
lam_xy = (3280961.71747429,3181078.06460131)
lonLat_WGS84 = (-88.4656575519999,41.76784005)
webMerc_xy = (-9847951.9514,5126266.20)
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy
        )
SG_well_dictionary[well_name] = well

#HEARTLAND DRIVE
dat_file = "Heartland_Drive.dat"
well_name = "HEARTLAND DRIVE"
p_num = 494075
aquifer = "silurian dolomite"
top_of_casing = 719.71
stick_up = 1.40
lam_xy = (3282116.38970564,3188847.54217256)
lonLat_WGS84 = (-88.4610802399999,41.789216976)
webMerc_xy = (-9847442.40729999,5129457.2774)
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy
        )
SG_well_dictionary[well_name] = well

#SUGR-18-03
dat_file = "Nagel_S_Curve.dat"
well_name = "SUGR-18-03"
p_num = 498310
aquifer = "st. charles bedrock valley"
top_of_casing = 711.08
stick_up = -0.53
lam_xy = (3281717.796015,3172144.197627)
lonLat_WGS84 = (-88.463249,41.743193)
webMerc_xy = (-9847683.8064,5122588.3365)
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy
        )
SG_well_dictionary[well_name] = well

#ISGS-HANNAFORD TRAIL
dat_file = "Hannaford_Trail.dat"
well_name = "ISGS-HANNAFORD TRAIL"
p_num = 498300
aquifer = "st. charles bedrock valley"
top_of_casing = 715.98
stick_up = 0.00 #?
lam_xy = (3285436.041531,3193360.256572)
lonLat_WGS84 = (-88.448663,41.801549)
webMerc_xy = (-9846060.1716,5131298.629)
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy
        )
SG_well_dictionary[well_name] = well

#print(GRL_well_dictionary[well_name].well_name)
#GRL_well_dictionary[well_name].gen_mpl_hydrograph()
#print(type(df['TIMESTAMP'][0]))
#GRL_well_dictionary[well_name].gen_hydrograph_csv()
