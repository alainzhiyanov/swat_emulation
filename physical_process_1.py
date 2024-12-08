"""
SWaT sub1 physical process

RawWaterTank has an inflow pipe and outflow pipe, both are modeled according
to the equation of continuity from the domain of hydraulics
(pressurized liquids) and a drain orefice modeled using the Bernoulli's
principle (for the trajectories).
"""

from minicps.devices import Tank

# from utils import PUMP_FLOWRATE_IN, PUMP_FLOWRATE_OUT
# from utils import TANK_HEIGHT, TANK_SECTION, TANK_DIAMETER
from utils import RWT_INIT_LEVEL, TANK_SECTION, STATE
from utils import PP_PERIOD_SEC, PP_PERIOD_HOURS, PP_SAMPLES
import pandas as pd
import os.path
import shutil
from utils import IP

import sys
import time
from datetime import datetime

import subprocess

# TODO: implement orefice drain with Bernoulli/Torricelli formula
class RawWaterTank(Tank):

    def pre_loop(self):
        time.sleep(5)
        print('DEBUG: Physical process begins')

        init = [505,890,900,200,200]

        self.result = []
        self.result.append(init)


    def Actuator(self, php): #
        # print(php.logdf.to_string())
        php.logdf.loc['P1.MV101.DI_ZSO','Value'] = php.logdf.loc['P1.MV101.DO_Open','Value']
        # P1.MV101.DI_ZSO = P1.MV101.DO_Open
        php.logdf.loc['P1.MV101.DI_ZSC','Value'] = php.logdf.loc['P1.MV101.DO_Close','Value']
        # P1.MV101.DI_ZSC = P1.MV101.DO_Close
        # php.logdf.loc['P2.MV201.DI_ZSO','Value'] = php.logdf.loc['P2.MV201.DO_Open','Value']
        # # P2.MV201.DI_ZSO = P2.MV201.DO_Open
        # php.logdf.loc['P2.MV201.DI_ZSC','Value'] = php.logdf.loc['P2.MV201.DO_Close','Value']
        # # P2.MV201.DI_ZSC = P2.MV201.DO_Close
        # php.logdf.loc['P3.MV301.DI_ZSO','Value'] = php.logdf.loc['P3.MV301.DO_Open','Value']
        # # P3.MV301.DI_ZSO = P3.MV301.DO_Open
        # php.logdf.loc['P3.MV301.DI_ZSC','Value'] = php.logdf.loc['P3.MV301.DO_Close','Value']
        # # P3.MV301.DI_ZSC = P3.MV301.DO_Close
        # php.logdf.loc['P3.MV302.DI_ZSO','Value'] = php.logdf.loc['P3.MV302.DO_Open','Value']
        # # P3.MV302.DI_ZSO = P3.MV302.DO_Open
        # php.logdf.loc['P3.MV302.DI_ZSC','Value'] = php.logdf.loc['P3.MV302.DO_Close','Value']
        # # P3.MV302.DI_ZSC = P3.MV302.DO_Close
        # php.logdf.loc['P3.MV303.DI_ZSO','Value'] = php.logdf.loc['P3.MV303.DO_Open','Value']
        # # P3.MV303.DI_ZSO = P3.MV303.DO_Open
        # php.logdf.loc['P3.MV303.DI_ZSC','Value'] = php.logdf.loc['P3.MV303.DO_Close','Value']
        # # P3.MV303.DI_ZSC = P3.MV303.DO_Close
        # php.logdf.loc['P3.MV304.DI_ZSO','Value'] = php.logdf.loc['P3.MV304.DO_Open','Value']
        # # P3.MV304.DI_ZSO = P3.MV304.DO_Open
        # php.logdf.loc['P3.MV304.DI_ZSC','Value'] = php.logdf.loc['P3.MV304.DO_Close','Value']
        # # P3.MV304.DI_ZSC = P3.MV304.DO_Close
        # php.logdf.loc['P5.MV501.DI_ZSO','Value'] = php.logdf.loc['P5.MV501.DO_Open','Value']
        # # P5.MV501.DI_ZSO = P5.MV501.DO_Open
        # php.logdf.loc['P5.MV501.DI_ZSC','Value'] = php.logdf.loc['P5.MV501.DO_Close','Value']
        # # P5.MV501.DI_ZSC = P5.MV501.DO_Close
        # php.logdf.loc['P5.MV502.DI_ZSO','Value'] = php.logdf.loc['P5.MV502.DO_Open','Value']
        # # P5.MV502.DI_ZSO = P5.MV502.DO_Open
        # php.logdf.loc['P5.MV502.DI_ZSC','Value'] = php.logdf.loc['P5.MV502.DO_Close','Value']
        # # P5.MV502.DI_ZSC = P5.MV502.DO_Close
        # php.logdf.loc['P5.MV503.DI_ZSO','Value'] = php.logdf.loc['P5.MV503.DO_Open','Value']
        # # P5.MV503.DI_ZSO = P5.MV503.DO_Open
        # php.logdf.loc['P5.MV503.DI_ZSC','Value'] = php.logdf.loc['P5.MV503.DO_Close','Value']
        # # P5.MV503.DI_ZSC = P5.MV503.DO_Close
        # php.logdf.loc['P5.MV504.DI_ZSO','Value'] = php.logdf.loc['P5.MV504.DO_Open','Value']
        # # P5.MV504.DI_ZSO = P5.MV504.DO_Open
        # php.logdf.loc['P5.MV504.DI_ZSC','Value'] = php.logdf.loc['P5.MV504.DO_Close','Value']
        # P5.MV504.DI_ZSC = P5.MV504.DO_Close

        # P1.P101.DI_Run = P1.P101.DO_Start
        php.logdf.loc['P1.P101.DI_Run','Value'] = php.logdf.loc['P1.P101.DO_Start','Value']
        # P1.P102.DI_Run = P1.P102.DO_Start
        php.logdf.loc['P1.P102.DI_Run','Value'] = php.logdf.loc['P1.P102.DO_Start','Value']
        # P3.P301.DI_Run = P3.P301.DO_Start
        # php.logdf.loc['P3.P301.DI_Run','Value'] = php.logdf.loc['P3.P301.DO_Start','Value']
        # # P3.P302.DI_Run = P3.P302.DO_Start
        # php.logdf.loc['P3.P302.DI_Run','Value'] = php.logdf.loc['P3.P302.DO_Start','Value']
        # # P4.P401.DI_Run = P4.P401.DO_Start
        # php.logdf.loc['P4.P401.DI_Run','Value'] = php.logdf.loc['P4.P401.DO_Start','Value']
        # # P4.P402.DI_Run = P4.P402.DO_Start
        # php.logdf.loc['P4.P402.DI_Run','Value'] = php.logdf.loc['P4.P402.DO_Start','Value']
        # # P5.P501.DI_Run = P5.P501_VSD_Out.Start or not P5.P501_VSD_Out.Stop
        # php.logdf.loc['P5.P501.DI_Run','Value'] = int(int(php.logdf.loc['P5.P501_VSD_Out.Start','Value']) or not int(php.logdf.loc['P5.P501_VSD_Out.Stop','Value']))
        # # P5.P502.DI_Run = P5.P502_VSD_Out.Start or not P5.P502_VSD_Out.Stop
        # php.logdf.loc['P5.P502.DI_Run','Value'] = int(int(php.logdf.loc['P5.P502_VSD_Out.Start','Value']) or not int(php.logdf.loc['P5.P502_VSD_Out.Stop','Value']))
        # # P6.P601.DI_Run = P6.P601.DO_Start
        # php.logdf.loc['P6.P601.DI_Run','Value'] = php.logdf.loc['P6.P601.DO_Start','Value']
        # # P6.P602.DI_Run = P6.P602.DO_Start
        # php.logdf.loc['P6.P602.DI_Run','Value'] = php.logdf.loc['P6.P602.DO_Start','Value']

    def Plant(self, php, datafile):

        self.h_t101=0
        self.h_t301=0
        self.h_t401=0
        self.h_t601=0
        self.h_t602=0
        self.p = {"f_mv101":2.3*1000000000/3600,"S_t101":1.5*1000000,"S_t301":1.5*1000000,"S_t401":1.5*1000000,"S_t501":1.5*1000000,"S_t601":1.5*1000000,"S_t602":1.5*1000000,"f_p101":2.0*1000000000/3600,"f_mv201":2.0*1000000000/3600,"f_p301":2.0*1000000000/3600,"f_mv302":2.0*1000000000/3600,"f_p602":2.0*1000000000/3600,"f_p401":2.0*1000000000/36001,"f_mv501":2.0*1000000000/3600,"f_mv502":0.00006111,"f_mv503":0.00049,"f_p601":2.0*1000000000/36001,"LIT101_AL":0.2,"LIT101_AH":0.8,"LIT301_AL":0.2,"LIT301_AH":0.8,"LIT401_AL":0.2,"LIT401_AH":0.8,"LIT601_AL":0.2,"LIT601_AH":0.8,"LIT602_AL":0.2,"LIT602_AH":0.8,"cond_AIT201_AL":250,"cond_AIT201_AH":260,"ph_AIT202_AL":6.95,"ph_AIT202_AH":7.05,"orp_AIT203_AL":420,"orp_AIT203_AH":500,"cond_AIT503_AH":260,"h201_AL":50,"h202_AL":4,"h203_AL":15,"cond_AIT503_AL":250,"cond_AIT503_AH":260,"orp_AIT402_AL":420,"orp_AIT402_AH":500,"omega_inlet":0.001}  # critical plant parameters

        #MV101, filling water into tank101
        if int(php.logdf.loc['P1.MV101.DI_ZSO','Value']) == 1:
            delta_t101 =  self.p['f_mv101'] / self.p['S_t101']
            self.h_t101=self.h_t101+delta_t101
            # print('delta_t101: ', delta_t101)

        #P101, drawing water from tank101
        if int(php.logdf.loc['P1.P101.DI_Run','Value']) == 1 or int(php.logdf.loc['P1.P102.DI_Run','Value']) == 1:
            delta_t101 =  0 - (self.p['f_p101'] / self.p['S_t101'])
            self.h_t101=self.h_t101+delta_t101
            # print('delta_t101: ', delta_t101)

        #mv201, feeding water to tank301
        # if int(php.logdf.loc['P2.MV201.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P1.P101.DI_Run','Value']) == 1:
        #     self.h_t301=self.h_t301+self.p['f_mv201'] / self.p['S_t301']
        #
        # #p301, drawing water from tank301
        # if int(php.logdf.loc['P3.P301.DI_Run','Value']) == 1 or int(php.logdf.loc['P3.P302.DI_Run','Value']) == 1:
        #     self.h_t301=self.h_t301-self.p['f_p301'] / self.p['S_t301']
        #
        # #UF flushing procedure, 30 sec
        # if int(php.logdf.loc['P3.P301.DI_Run','Value']) == 1 or int(php.logdf.loc['P3.P302.DI_Run','Value']) == 1 and int(php.logdf.loc['P3.MV301.DI_ZSC','Value']) and  int(php.logdf.loc['P3.MV302.DI_ZSC','Value']) and int(php.logdf.loc['P3.MV303.DI_ZSC','Value']) and int(php.logdf.loc['P3.MV304.DO_ZSO','Value']) and int(php.logdf.loc['P6.P602.DI_Run','Value']) == 0:
        #     pass
        # if int(php.logdf.loc['P3.P301.DI_Run','Value']) == 1 or int(php.logdf.loc['P3.P302.DI_Run','Value']) == 1 and int(php.logdf.loc['P3.MV301.DI_ZSC','Value']) == 1 and  int(php.logdf.loc['P3.MV302.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P3.MV303.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P3.MV304.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P6.P602.DI_Run','Value']) == 0:   #UF ultra filtration procedure, 30 min
        #     self.h_t401=self.h_t401+ self.p['f_mv302'] / self.p['S_t401']
        #     # print int(php.logdf.loc['P3.P301.DI_Run','Value']),  int(php.logdf.loc['P3.P302.DI_Run','Value']),  int(php.logdf.loc['P3.MV301.DI_ZSC','Value']),   int(php.logdf.loc['P3.MV302.DI_ZSO','Value']),  int(php.logdf.loc['P3.MV303.DI_ZSC','Value']),  int(php.logdf.loc['P3.MV304.DI_ZSC','Value']),  int(php.logdf.loc['P6.P602.DI_Run','Value'])
        #     # print 'Tank4 ++'
        # # else:
        # #     print int(php.logdf.loc['P3.P301.DI_Run','Value']),  int(php.logdf.loc['P3.P302.DI_Run','Value']),  int(php.logdf.loc['P3.MV301.DI_ZSC','Value']),   int(php.logdf.loc['P3.MV302.DI_ZSO','Value']),  int(php.logdf.loc['P3.MV303.DI_ZSC','Value']),  int(php.logdf.loc['P3.MV304.DI_ZSC','Value']),  int(php.logdf.loc['P6.P602.DI_Run','Value'])
        #
        # if int(php.logdf.loc['P3.P301.DI_Run','Value']) == 0 and int(php.logdf.loc['P3.P302.DI_Run','Value']) == 0 and int(php.logdf.loc['P3.MV301.DI_ZSO','Value']) == 1 and  int(php.logdf.loc['P3.MV302.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P3.MV303.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P3.MV304.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P6.P602.DI_Run','Value']) == 1:   #UF back wash procedure, 45 sec
        #     self.h_t602=self.h_t602- self.p['f_p602'] / self.p['S_t602']
        # if int(php.logdf.loc['P3.P301.DI_Run','Value']) == 0 and int(php.logdf.loc['P3.P302.DI_Run','Value']) == 0 and int(php.logdf.loc['P3.MV301.DI_ZSC','Value']) == 1 and  int(php.logdf.loc['P3.MV302.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P3.MV303.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P3.MV304.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P6.P602.DI_Run','Value']) == 0:   #UF feed tank draining procedure, 1 min
        #     pass
        #
        # if int(php.logdf.loc['P4.P401.DI_Run','Value']) == 1 or int(php.logdf.loc['P4.P402.DI_Run','Value']) == 1: #P401, drawing water from t401
        #     self.h_t401=self.h_t401- self.p['f_p401'] / self.p['S_t401']
        #     # print 'Tank4 --'
        #
        # if int(php.logdf.loc['P4.P401.DI_Run','Value']) == 1 or int(php.logdf.loc['P4.P402.DI_Run','Value']) == 1 and int(php.logdf.loc['P5.P501.DI_Run','Value']) == 1 or int(php.logdf.loc['P5.P502.DI_Run','Value']) == 1 and int(php.logdf.loc['P5.MV501.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P5.MV502.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P5.MV503.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P5.MV504.DI_ZSC','Value']) == 1:#procedure for RO normal functioning with product of permeate 60% and backwash 40%
        #     self.h_t601=self.h_t601+self.p['f_mv501'] / self.p['S_t601']
        #     self.h_t602=self.h_t602+self.p['f_mv502'] / self.p['S_t602']
        # elif int(php.logdf.loc['P4.P401.DI_Run','Value']) == 1 or int(php.logdf.loc['P4.P402.DI_Run','Value']) == 1 and int(php.logdf.loc['P5.P501.DI_Run','Value']) == 1 or int(php.logdf.loc['P5.P502.DI_Run','Value']) == 1 and int(php.logdf.loc['P5.MV501.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P5.MV502.DI_ZSC','Value']) == 1 and int(php.logdf.loc['P5.MV503.DI_ZSO','Value']) == 1 and int(php.logdf.loc['P5.MV504.DI_ZSO','Value']) == 1:#procedure for RO flushing with product of backwash 60% and drain 40%
        #     self.h_t602=self.h_t602+self.p['f_mv503'] / self.p['S_t602']
        # if int(php.logdf.loc['P6.P601.DI_Run','Value']) == 1: # Pumping water out of tank601
        #     self.h_t601=self.h_t601-self.p['f_p601'] / self.p['S_t601']


        php.logdf.loc['HMI_LIT101_Pv','Value'] = self.result[php.k][0]
        # HMI.LIT101.set_alarm()

        # php.logdf.loc['HMI_LIT301_Pv','Value'] = self.result[php.k][1]
        # # HMI.LIT301.set_alarm()
        #
        # php.logdf.loc['HMI_LIT401_Pv','Value'] = self.result[php.k][2]
        # # HMI.LIT401.set_alarm()
        # datafile.write(str(datetime.now().strftime("%m/%d/%Y-%H:%M:%S.%f"))+','+str(self.result[php.k][0])+','+str(self.result[php.k][1])+','+str(self.result[php.k][2])+'\n')
        #
        #
        # if self.result[php.k][3]>700:
        #     php.logdf.loc['HMI_LSH601_Alarm','Value'] = 1
        #
        # if self.result[php.k][3]<200:
        #     php.logdf.loc['HMI_LSL601_Alarm','Value'] = 1
        #
        #
        # if self.result[php.k][4]>700:
        #     php.logdf.loc['HMI_LSH601_Alarm','Value'] = 1
        #
        # if self.result[php.k][4]<200:
        #     php.logdf.loc['HMI_LSL601_Alarm','Value'] = 1

        new_result = [0 for x in range(5)]
        new_result[0] = self.result[php.k][0]+self.h_t101*php.time_interval
        # new_result[1] = self.result[php.k][1] + self.h_t301 * php.time_interval
        # new_result[2] = self.result[php.k][2] + self.h_t401 * php.time_interval
        # new_result[3] = self.result[php.k][3] + self.h_t601 * php.time_interval
        # new_result[4] = self.result[php.k][4] + self.h_t602 * php.time_interval
        self.result.append(new_result)

        # Sending updated P1.P101.DI_Run value to the other SubProcess
        subprocess.call(["python", "./client_plc1.py", IP['plcx'], str(int(php.logdf.loc['P1.P101.DI_Run','Value']))])


        print (self.result[php.k][0:5])
        php.k = php.k + 1


    def main_loop(self):
        self.k = 0
        self.time_interval=1

        self.processctr = 0
        self.logdf = pd.DataFrame()

        datafile = open('TankLevelReadings_1.csv','a')
        datafile.write("Time,Tank1,Tank3,Tank4\n")
        while(True):
            if self.processctr == 0:
                logname = './log_'+str(self.processctr)+'_1.csv'
            else:
                logname = './log_'+str(self.processctr)+'_1.pkl'
            while not os.path.exists(logname):
                time.sleep(0.0001)

            if self.processctr == 0:
                self.logdf = pd.read_csv(logname)
                self.logdf = self.logdf.set_index('Tag')
            else:
                self.logdf = pd.read_pickle(logname)

            self.logdf['Value'] = self.logdf['Value'].astype(float)

            self.Actuator(self)
            self.Plant(self,datafile)

            newlogname = './log_'+str(self.processctr)+'_plc1.pkl'
            self.logdf.to_pickle(newlogname)
            self.logdf = pd.DataFrame()
            if self.processctr > 0:
                histlogname = './historian/log_'+str(self.processctr)+'_plc1.pkl'
                shutil.move(logname,histlogname)
            self.processctr = self.processctr + 1
            # time.sleep(PP_PERIOD_SEC)
            # time.sleep(1)

        datafile.close()


if __name__ == '__main__':

    rwt = RawWaterTank(
        name='rwt',
        state=STATE,
        protocol=None,
        section=TANK_SECTION,
        level=RWT_INIT_LEVEL
    )
