# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:29:43 2019

@author: iordach1
"""
import pandas as pd
from GRL_well_class import GRL_Well


GRL_well_dictionary = {}

# BUR 95C
dat_file = "BUR 95C_Hourly.dat"
well_name = "BUR-95C"
p_num = 381676
aquifer = "sankoty"
top_of_casing = 577.90
top_of_aq = top_of_casing - 53  #from boring log
lam_xy = (2999698.85644471,3033900.63914047)
lonLat_WGS84 = (-89.50117976,41.36651101)
webMerc_xy = (-9963225.75660000,5066553.19020000)
nested = False
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#HRY 91C
dat_file = "HRY 91C & D_Hourly.dat"
well_name = "HRY-91C"
p_num = 381651
aquifer = "sankoty"
top_of_casing = 613.65
top_of_aq = top_of_casing - 66   #from boring log
lam_xy = (2880881.68856772,3072065.43945114)
lonLat_WGS84 = (-89.93673191,41.47094837)
webMerc_xy = (-10011711.19989990,5082056.58829999)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#HRY 91D
dat_file = "HRY 91C & D_Hourly.dat"
well_name = "HRY-91D"
p_num = 381652
aquifer = "tampico"
top_of_casing = 613.82
top_of_aq = top_of_casing - 1.4 #from boring log
lam_xy = (2880893.07798063,3072065.38334889)
lonLat_WGS84 = (-89.93669016,41.47094837)
webMerc_xy = (-10011706.55220000,5082056.58789999)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#WTS 91G
dat_file = "WTS 91 G&H_Hourly.dat"
well_name = "WTS-91G"
p_num = 381645
aquifer = "sankoty"
top_of_casing = 642.75
top_of_aq = top_of_casing - 68 #from boring log
lam_xy = (2932200.71453838,3160203.30549789)
lonLat_WGS84 = (-89.74950437,41.71445477)
webMerc_xy = (-9990869.12529999,5118301.66009999)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#WTS 91H
dat_file = "WTS 91 G&H_Hourly.dat"
well_name = "WTS-91H"
p_num = 381646
aquifer = "tampico"
top_of_casing = 642.67
top_of_aq = top_of_casing - 4 #from boring log
lam_xy = (2932192.98456697,3160203.87669098)
lonLat_WGS84 = (-89.74953281,41.71445628)
webMerc_xy = (-9990872.29150000,5118301.88610000)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#WTS 91E
dat_file = "WTS-91 E & F_Hourly.dat"
well_name = "WTS-91E"
p_num = 381643
aquifer = "sankoty"
top_of_casing = 616.33
top_of_aq = top_of_casing - 70 #from boring log
lam_xy = (2895972.75681072,3131330.63030372)
lonLat_WGS84 = (-89.88233043,41.63451925)
webMerc_xy = (-10005655.25469990,5106388.45380000)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#WTS 91F
dat_file = "WTS-91 E & F_Hourly.dat"
well_name = "WTS-91F"
p_num = 381644
aquifer = "tampico"
top_of_casing = 617.55
top_of_aq = top_of_casing - 1.8 #from boring log
lam_xy = (2895972.78765055,3131336.17589631)
lonLat_WGS84 = (-89.88233040,41.63453454)
webMerc_xy = (-10005655.25170000,5106390.73070000)
nested = True
well = GRL_Well(
            dat_file = dat_file,
            well_name = well_name,
            p_num = p_num,
            aquifer = aquifer,
            top_of_casing = top_of_casing,
            top_of_aq = top_of_aq,
            lam_xy = lam_xy,
            lonLat_WGS84 = lonLat_WGS84,
            webMerc_xy = webMerc_xy,
            nested = nested
        )
GRL_well_dictionary[well_name] = well

#print(GRL_well_dictionary[well_name].well_name)
#GRL_well_dictionary[well_name].gen_mpl_hydrograph()
#print(type(df['TIMESTAMP'][0]))
#GRL_well_dictionary[well_name].gen_hydrograph_csv()
