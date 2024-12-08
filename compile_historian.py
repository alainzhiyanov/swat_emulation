# File Name: compile_historian.py
# Author: Gargi Mitra
# Functionality: Compiling historian record from a set of pickle files generated during emulation
# Input: path to input directory containing set of pickle files, output directory
# Output: A single excel file with compiled historian records
# Error checking has not been implemented in this version. Make sure input directory exists
# Command Syntax: python compile_historian.py -in <path_to_historian_directory_containing_pickle_files> -out <path_to_output_directory>
# Sample command: python compile_historian.py -in /home/gargi/Desktop/ASIACCS-2023/Results-nodb/first_successful_run/historian -out /home/gargi/Desktop/ASIACCS-2023/Results-nodb/first_successful_run

import io
import os
import sys
import pickle
from datetime import datetime
import time
import datetime
import glob
import pandas as pd
import csv

########################## take input parameters ################################
def exit_with_help(error=''):
    print("""\
Usage: compile_historian.py [options]

options:
    -in { /in/ } : path to input directory
    -out { /out/ } : path to output directory
 """)
    print(error)
    sys.exit(1)

#################################################################################

# Arguments to be read from command line
args = [ ('in', 'in', 'in'),
         ('out', 'out', 'out')]

# Checking if all variables are/will be set
for var, env, arg in args:
    if not '-'+arg in sys.argv:
        vars()[var] = os.getenv(env)
        if vars()[var] == None:
            exit_with_help('Error: Environmental Variables or Argument'+
                        ' insufficiently set! ($'+env+' / "-'+arg+'")')

# Read parameters from command line call
if len(sys.argv) != 0:
    i = 0
    options = sys.argv[1:]
    # iterate through parameters
    while i < len(options):
        if options[i] == '-in':
                i = i + 1
                path_to_pickles = options[i]
        elif options[i] == '-out':
                i = i + 1
                outputpath = options[i]
        else:
            exit_with_help('Error: Unknown Argument! ('+ options[i] + ')')
        i = i + 1

if not path_to_pickles.endswith('/'):
    path_to_pickles = path_to_pickles + '/'

if not outputpath.endswith('/'):
    outputpath = outputpath + '/'
try:
    if not os.path.isdir(outputpath):
        os.makedirs(outputpath)
except:
    print ("Error in creating output path")
    sys.exit(1)

#################################################################################
#################################################################################
########################### compile historian ###################################
#################################################################################
#################################################################################

# Sort filenames by modification time and merge
outFile = open(outputpath+'historian.csv', 'a+')
writer = csv.writer(outFile)
headers = ['Timestamp','HMI_LIT101_AHH', 'HMI_LIT101_Pv', 'P1.MV101.DI_ZSO', 'P1.MV101.DI_ZSC', 'P1.MV101.DO_Open', 'P1.MV101.DO_Close', 'P1.P101.DI_Run', 'P1.P101.DO_Start', 'P1.P102.DI_Run', 'P1.P102.DO_Start', 'HMI_PLANT_STOP', 'HMI_PLANT_START', 'HMI_LIT_301_AL', 'HMI_LIT_301_AH', 'HMI_PLANT_RESET_ON', 'HMI_PLANT_AUTO_ON', 'HMI_PLANT_AUTO_OFF', 'HMI_P2_PERMISSIVE_ON', 'HMI_P3_PERMISSIVE_ON', 'HMI_P4_PERMISSIVE_ON', 'HMI_PLANT_READY', 'HMI_MV201_STATUS', 'HMI_LIT301_Pv', 'HMI_LIT401_Pv', 'HMI_LSH601_Alarm', 'HMI_LSL601_Alarm', 'P2.MV201.DI_ZSO', 'P2.MV201.DO_Open', 'P2.MV201.DI_ZSC', 'P2.MV201.DO_Close', 'P3.P301.DI_Run', 'P3.P302.DI_Run', 'P3.MV301.DI_ZSC', 'P3.MV302.DI_ZSC', 'P3.MV303.DI_ZSC', 'P3.MV304.DO_ZSO', 'P3.MV304.DI_ZSO', 'P3.MV302.DI_ZSO', 'P3.MV303.DI_ZSO', 'P3.MV304.DI_ZSC', 'P3.MV301.DI_ZSO', 'P3.P301.DO_Start', 'P3.P302.DO_Start', 'P3.MV301.DO_Open', 'P3.MV302.DO_Open', 'P3.MV303.DO_Open', 'P3.MV304.DO_Open', 'P3.MV301.DO_Close', 'P3.MV302.DO_Close', 'P3.MV303.DO_Close', 'P3.MV304.DO_Close', 'P4.P401.DI_Run', 'P4.P401.DO_Start', 'P4.P402.DI_Run', 'P4.P402.DO_Start', 'P5.MV501.DI_ZSO', 'P5.MV501.DO_Open', 'P5.MV501.DI_ZSC', 'P5.MV501.DO_Close', 'P5.MV502.DI_ZSO', 'P5.MV502.DO_Open', 'P5.MV502.DI_ZSC', 'P5.MV502.DO_Close', 'P5.MV503.DI_ZSO', 'P5.MV503.DO_Open', 'P5.MV503.DI_ZSC', 'P5.MV503.DO_Close', 'P5.MV504.DI_ZSO', 'P5.MV504.DO_Open', 'P5.MV504.DI_ZSC', 'P5.MV504.DO_Close', 'P5.P501.DI_Run', 'P5.P501_VSD_Out.Start', 'P5.P502.DI_Run', 'P5.P501_VSD_Out.Stop', 'P5.P502_VSD_Out.Start', 'P5.P502_VSD_Out.Stop', 'P6.P601.DI_Run', 'P6.P601.DO_Start', 'P6.P602.DI_Run', 'P6.P602.DO_Start']
writer.writerow(headers)

logdf = pd.DataFrame()

list_of_files = filter( os.path.isfile, glob.glob(path_to_pickles + '*') )
list_of_files = sorted( list_of_files, key = os.path.getmtime)
for file_path in list_of_files:
    timestamp_str = time.strftime('%m/%d/%y %H:%M:%S %p', time.gmtime(os.path.getmtime(file_path)))
    print timestamp_str, file_path
    logdf = pd.read_pickle(file_path)
    logdf = logdf.reset_index()
    logdf = logdf.T
    values = logdf.iloc[1].to_list()
    values.insert(0, timestamp_str)
    print values
    writer.writerow(values)

outFile.close()
