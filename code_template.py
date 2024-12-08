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
