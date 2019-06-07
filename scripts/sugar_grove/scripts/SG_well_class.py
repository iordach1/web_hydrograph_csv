# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:10:15 2019

@author: iordach1
"""
import pandas as pd
import matplotlib.pyplot as plt

class SG_Well:
    
    #"private" attributes and methods
    __dat_dir = r"\\swshydro\Data"'\\'
    __output_dir = r"\\SWSTURBULENCE\data\sugar_grove"'\\'
    
    def __gen_telemetry_dataframe(self):
        df = pd.read_csv(self.__dat_location, skiprows = [2,3], header = 1)
        
        if self.nested:
            df.rename(columns = {"Water_level":"sankoty_water_level", "WaterLevel":"tampico_water_level"}, inplace = True)
        else:   df.rename(columns = {"WaterLevel":"sankoty_water_level"}, inplace = True)
        
        return df
    
    def __gen_hydrograph_df(self):
        if self.aquifer == 'SANKOTY':
            df = self.telemetry_df[['TIMESTAMP', 'sankoty_water_level']]
            df['head'] = self.ground_surface - pd.to_numeric(df['sankoty_water_level'], errors = 'coerce')
            df['depth_to_water_from_land_surface'] = pd.to_numeric(df['sankoty_water_level'], errors = 'coerce') - (self.top_of_casing - self.ground_surface)
        else: 
            df = self.telemetry_df[['TIMESTAMP', 'tampico_water_level']]
            df['head'] = self.ground_surface - pd.to_numeric(df['tampico_water_level'], errors = 'coerce')
            df['depth_to_water_from_land_surface'] = pd.to_numeric(df['tampico_water_level'], errors = 'coerce') - (self.top_of_casing - self.ground_surface)
        
        df.drop_duplicates(subset = 'TIMESTAMP', keep = 'first', inplace = True)
        
        df = df.round({'head' : 2, 'depth_to_water_from_land_surface' : 2})
        
        return df 
    
    def gen_cc_csv(self):
        self.telemetry_df.to_csv(
                    path_or_buf = "{0}\\{1}\\{2}_{3}.csv".format(
                            self.__output_dir,
                            "carbon_copy_csv",
                            self.p_num,
                            self.well_name
                        ),
                    index = False
                )

    def gen_hydrograph_csv(self):
        self.__gen_hydrograph_df()[['TIMESTAMP', 'depth_to_water_from_land_surface', 'head']].to_csv(
                    path_or_buf = self.__hyd_csv_path,
                    index_label = 'RECORD'
                )
        
    def gen_mpl_hydrograph(self):
        df = pd.read_csv(
                filepath_or_buffer = self.__hyd_csv_path, 
                usecols = ['TIMESTAMP', 'head'],
                parse_dates = ['TIMESTAMP'],
                infer_datetime_format = True
                )
        plt.scatter(df['TIMESTAMP'], df['head'], s = 5)
        plt.title(self.well_name)
        plt.xticks(rotation = 70)
        plt.ylabel("Head (ft) -- {0} aquifer".format(self.aquifer.title()))
        plt.tight_layout()
        plt.savefig(fname = self.__mpl_hyd_path)
        plt.clf()
    
    def __init__(self, dat_file, well_name, p_num, aquifer, top_of_casing, stick_up, lam_xy, lonLat_WGS84, webMerc_xy) :
        self.dat_file = dat_file
        self.__dat_location = self.__dat_dir + self.dat_file
        self.well_name = well_name
        self.p_num = p_num
        self.aquifer = aquifer.upper()
        self.top_of_casing = top_of_casing
        self.ground_surface = top_of_casing - stick_up
        self.lam_xy = lam_xy
        self.lonLat_WGS84 = lonLat_WGS84
        self.webMerc_xy = webMerc_xy
        self.telemetry_df = self.__gen_telemetry_dataframe()
        self.__hyd_csv_path = "{0}\\{1}\\{2}_{3}_hyd.csv".format(
                            self.__output_dir,
                            "web_hydrograph_csv",
                            self.p_num,
                            self.well_name
                        )
        self.__mpl_hyd_path = "{0}\\{1}\\{2}_{3}_hyd.jpg".format(
                            self.__output_dir,
                            "mpl_hydrographs",
                            self.p_num,
                            self.well_name
                        )
        