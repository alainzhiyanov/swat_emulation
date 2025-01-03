# SCADA is the control interface, talking and giving instructions to all PLCs
from HMI.HMI import *
from utils import IP
PLCX_ADDR = IP['plcx']

class H:
  def __init__(self, plc):
		# Whole PLANT
        self.PLANT = HMI_plant()
        self.PLC = plc
        self.PLC.logdf.loc['HMI_PLANT_RESET_ON','Value'] = 1
        self.PLC.logdf.loc['HMI_PLANT_AUTO_ON','Value'] = 1
        self.PLC.logdf.loc['HMI_PLANT_AUTO_OFF','Value'] = 0
        self.PLC.logdf.loc['HMI_PLANT_READY','Value'] = 1
        self.PLC.logdf.loc['HMI_PLANT_STOP','Value'] = 0
        self.PLC.logdf.loc['HMI_PLANT_START','Value'] = 1
        self.PLC.send(('HMI_PLANT_RESET_ON',2),1,PLCX_ADDR)
        self.PLC.send(('HMI_PLANT_AUTO_ON',2),1,PLCX_ADDR)
        self.PLC.send(('HMI_PLANT_AUTO_OFF',2),0,PLCX_ADDR)
        self.PLC.send(('HMI_PLANT_READY',2),1,PLCX_ADDR)
        self.PLC.send(('HMI_PLANT_STOP',2),0,PLCX_ADDR)
        self.PLC.send(('HMI_PLANT_START',2),1,PLCX_ADDR)

        # self.P1 = HMI_phase()
        self.P2 = HMI_phase()
        self.PLC.logdf.loc['HMI_P2_PERMISSIVE_ON','Value'] = 1
        self.PLC.send(('HMI_P2_PERMISSIVE_ON',2),1,PLCX_ADDR)

        self.P3 = HMI_phase()
        self.PLC.logdf.loc['HMI_P3_PERMISSIVE_ON','Value'] = 1
        self.PLC.send(('HMI_P3_PERMISSIVE_ON',2),1,PLCX_ADDR)

        self.P4 = HMI_phase()
        self.PLC.logdf.loc['HMI_P4_PERMISSIVE_ON','Value'] = 1
        self.PLC.send(('HMI_P4_PERMISSIVE_ON',2),1,PLCX_ADDR)

        self.P5 = HMI_phase()
        self.P6 = HMI_phase()
# P1
         # self.LIT101 = HMI_LIT(1100.0,800.0,500.0,250.0)
         # self.MV101  = HMI_mv()
         # self.FIT101 = HMI_FIT(3.0,2.6,2.5,0.0)
         # self.P101   = HMI_pump()
         # self.P102   = HMI_pump()
         # self.P_RAW_WATER_DUTY = HMI_duty2()
# P2
        self.MV201 = HMI_mv()
        self.PLC.logdf.loc['HMI_MV201_STATUS','Value'] = 1
        self.PLC.send(('HMI_MV201_STATUS',2),1,PLCX_ADDR)

        self.LS201 = HMI_LS()
        self.LS202 = HMI_LS()
        self.LSL203 = HMI_LS()
        self.LSLL203 = HMI_LS()
        self.P201  = HMI_pump()
        self.P202  = HMI_pump()
        self.P203  = HMI_pump()
        self.P204  = HMI_pump()
        self.P205  = HMI_pump()
        self.P206  = HMI_pump()
        self.P207  = HMI_pump()
        self.P208  = HMI_pump()
        self.P_NACL_DUTY = HMI_duty2()
        self.P_HCL_DUTY  = HMI_duty2()
        self.P_NAOCL_FAC_DUTY = HMI_duty2()
        self.FIT201 = HMI_FIT(4.0,2,0.5,0.0)
        self.AIT201 = HMI_ait(950.0, 260.0, 250.0,50.0)
        self.AIT202 = HMI_ait(12.0, 7.05,6.95,3.0)
        self.AIT203 = HMI_ait(750.0,500.0,420.0,100.0)
# self.P3
        self.Mid_P602_AutoInp = 0
        self.Cy_P3 = HMI_Ultralfiltration_Cycle()

        self.LIT301 = HMI_LIT(1200.0,1000.0,800.0,250.0)
        self.PLC.logdf.loc['HMI_LIT_301_AL','Value'] = 0
        self.PLC.send(('HMI_LIT_301_AL',2),0,PLCX_ADDR)
        self.PLC.logdf.loc['HMI_LIT_301_AH','Value'] = 0
        self.PLC.send(('HMI_LIT_301_AH',2),0,PLCX_ADDR)

        self.P301   = HMI_pump()
        self.P302   = HMI_pump()
        self.P_UF_FEED_DUTY = HMI_duty2()
        self.FIT301 = HMI_FIT(4.0,2.4,0.5,0.0)
        self.PSH301 = HMI_PSH()
        self.DPSH301 = HMI_DPSH()
        self.DPIT301 = HMI_DPIT(101.325,40.53,10.1325,0.0)
        self.MV301 = HMI_mv()
        self.MV302 = HMI_mv()
        self.MV303 = HMI_mv()
        self.MV304 = HMI_mv()
# self.P4
        self.LS401 = HMI_LS()
        self.LIT401 = HMI_LIT(1200.0,1000.0,800.0,250.0)
        self.P401  = HMI_pump()
        self.P402  = HMI_pump()
        self.P403  = HMI_pump()
        self.P404  = HMI_pump()
        self.UV401 = HMI_uv()
        self.P_NAHSO3_ORP_DUTY = HMI_duty2()
        self.P_RO_FEED_DUTY   = HMI_duty2()
        self.AIT401 = HMI_ait(100.0, 80.0, 0.0, 0.0)
        self.AIT402 = HMI_ait(800.0, 250.0, 240.0, 200.0)
        self.FIT401 = HMI_FIT(4.0,2.0,0.5,0.0)
# self.P5
        self.Mid_P603_AutoInp = 0 # This a variable shared and mostly read by P6 PLC, it's not HMI variable(maybe from SCADA, people can't change),but in our current PLC coding, Phase 5 is not writing to this variable, it keeps 0  --PF
        self.Cy_P5  = HMI_ReverseOsmosis_Cycle()
        self.AIT501 = HMI_ait(14.0,8.0,6.0,2.0)
        self.AIT502 = HMI_ait(300.0, 250.0, 0.0,0.0)
        self.AIT503 = HMI_ait(500.0,260.0,250.0,0.0)
        self.AIT504 = HMI_ait(15.0,10.0,0.0,0.0)
        self.PIT501 = HMI_PIT(0,0,0,0)
        self.PIT502 = HMI_PIT(0,0,0,0)
        self.PIT503 = HMI_PIT(0,0,0,0)
        self.FIT501 = HMI_FIT(4,2,1,0)
        self.FIT502 = HMI_FIT(4,1.3,1.1,0)
        self.FIT503 = HMI_FIT(4,0.9,0.7,0)
        self.FIT504 = HMI_FIT(2,0.35,0.25,0)
        self.MV501 = HMI_mv()
        self.MV502 = HMI_mv()
        self.MV503 = HMI_mv()
        self.MV504 = HMI_mv()
        self.P_RO_HIGH_DUTY = HMI_duty2()
        self.P501 = HMI_VSD()
        self.P502 = HMI_VSD()
# self.P6
        self.LSL601 = HMI_LSL()
        self.LSL602 = HMI_LSL()
        self.LSL603 = HMI_LSL()
        self.LSH601 = HMI_LSH()
        self.LSH602 = HMI_LSH()
        self.LSH603 = HMI_LSH()
        self.P601 = HMI_pump()
        self.P602 = HMI_pump()
        self.P603 = HMI_pump()
        self.FIT601 = HMI_FIT(4,3,2,0)
