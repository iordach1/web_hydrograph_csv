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
#aquifer = "sankoty"
#top_of_casing = 577.90
#stick_up = 2.60
#top_of_aq = top_of_casing - stick_up - 53  #from boring log
#lam_xy = (2999698.85644471,3033900.63914047)
#lonLat_WGS84 = (-89.50117976,41.36651101)
#webMerc_xy = (-9963225.75660000,5066553.19020000)
#nested = False
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
SG_well_dictionary[well_name] = well

#HEARTLAND DRIVE
dat_file = "Heartland_Drive.dat"
well_name = "HEARTLAND DRIVE"
p_num = 494075
#aquifer = "sankoty"
#top_of_casing = 613.65
#stick_up = 1.50
#top_of_aq = top_of_casing - stick_up - 66   #from boring log
#lam_xy = (2880881.68856772,3072065.43945114)
#lonLat_WGS84 = (-89.93673191,41.47094837)
#webMerc_xy = (-10011711.19989990,5082056.58829999)
#nested = True
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
SG_well_dictionary[well_name] = well

#SUGR-18-03
dat_file = "Nagel_S_Curve.dat"
well_name = "SUGR-18-03"
p_num = 498310
#aquifer = "tampico"
#top_of_casing = 613.82
#stick_up = 1.40
#top_of_aq = top_of_casing - stick_up #from boring log
#lam_xy = (2880893.07798063,3072065.38334889)
#lonLat_WGS84 = (-89.93669016,41.47094837)
#webMerc_xy = (-10011706.55220000,5082056.58789999)
#nested = True
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
SG_well_dictionary[well_name] = well

#ISGS-HANNAFORD TRAIL
dat_file = "Hannaford_Trail.dat"
well_name = "ISGS-HANNAFORD TRAIL"
p_num = 498300
#aquifer = "sankoty"
#top_of_casing = 642.75
#stick_up = 4.00
#top_of_aq = top_of_casing - stick_up - 68 #from boring log
#lam_xy = (2932200.71453838,3160203.30549789)
#lonLat_WGS84 = (-89.74950437,41.71445477)
#webMerc_xy = (-9990869.12529999,5118301.66009999)
#nested = True
well = SG_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            stick_up = stick_up,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
SG_well_dictionary[well_name] = well

#print(GRL_well_dictionary[well_name].well_name)
#GRL_well_dictionary[well_name].gen_mpl_hydrograph()
#print(type(df['TIMESTAMP'][0]))
#GRL_well_dictionary[well_name].gen_hydrograph_csv()
