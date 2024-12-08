"""
swat-s1 utils.py

sqlite and enip use name (string) and pid (int) has key and the state stores
values as strings.

sqlite uses float keyword and cpppo use REAL keyword.
"""

from minicps.utils import build_debug_logger

swat = build_debug_logger(
    name=__name__,
    bytes_per_file=10000,
    rotating_files=2,
    lformat='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    ldir='logs/',
    suffix='')


# PLC_PERIOD_SEC = 0.40  # plc update rate in seconds

PLC_PERIOD_SEC = 1  # plc update rate in seconds
PLC_PERIOD_HOURS = PLC_PERIOD_SEC / 3600.0
PLC_SAMPLES = 1000

PP_RESCALING_HOURS = 100
PP_PERIOD_SEC = 0.20  # physical process update rate in seconds
PP_PERIOD_HOURS = (PP_PERIOD_SEC / 3600.0) * PP_RESCALING_HOURS
PP_SAMPLES = int(PLC_PERIOD_SEC / PP_PERIOD_SEC) * PLC_SAMPLES

TANK_SECTION = 0
RWT_INIT_LEVEL = 100

# topo {{{1
IP = {
    'plc1': '192.168.1.10',
    # 'plc2': '192.168.1.20'
    # 'plc3': '192.168.1.30',
    # 'plc4': '192.168.1.40',
    # 'plc5': '192.168.1.50',
    # 'plc6': '192.168.1.60',
    'plcx': '192.168.1.70'
    # 'hist': '192.168.1.200',
    # 'workstation': '192.168.1.201'
}

NETMASK = '/24'

MAC = {
    'plc1': '00:1D:9C:C7:B0:70',
    # 'plc2': '00:1D:9C:C8:BC:46'
    # 'plc3': '00:1D:9C:C8:BD:F2',
    # 'plc4': '00:1D:9C:C7:FA:2C',
    # 'plc5': '00:1D:9C:C8:BC:2F',
    # 'plc6': '00:1D:9C:C7:FA:2D',
    'plcx': '00:1D:9C:C6:72:e8'
    # 'hist': '00:15:5D:01:9A:49',
    # 'workstation': '00:0C:29:74:0B:C7',
    # # 'attacker': 'AA:AA:AA:AA:AA:AA',
}


# others
# TODO
PLC1_DATA = {
'HMI_LIT101_AHH': '0',
'HMI_LIT101_Pv': '0',
'P1.MV101.DI_ZSO': '0',
'P1.MV101.DI_ZSC': '1',
'P1.MV101.DO_Open': '0',
'P1.MV101.DO_Close': '0',
'P1.P101.DI_Run': '0',
'P1.P101.DO_Start': '0',
'P1.P102.DI_Run': '0',
'P1.P102.DO_Start': '0'
}
# TODO
PLCX_DATA = {
    'HMI_PLANT_RESET_ON': '1',
    'HMI_PLANT_AUTO_ON': '1',
    'HMI_PLANT_AUTO_OFF': '0',
    'HMI_P2_PERMISSIVE_ON': '1',
    'HMI_P3_PERMISSIVE_ON': '1',
    'HMI_P4_PERMISSIVE_ON': '1',
    'HMI_PLANT_READY': '1',
    'HMI_MV201_STATUS': '1',
    'HMI_PLANT_STOP': '0',
    'HMI_PLANT_START': '1',
    'HMI_LIT_301_AL': '0',
    'HMI_LIT_301_AH': '0',
    'HMI_LIT301_Pv': '0',
    'HMI_LIT401_Pv': '0',
    'HMI_LSH601_Alarm': '0',
    'HMI_LSL601_Alarm': '0',
    'P2.MV201.DI_ZSO': '0',
    'P2.MV201.DO_Open': '0',
    'P2.MV201.DI_ZSC': '1',
    'P2.MV201.DO_Close': '0',
    'P3.P301.DI_Run': '0',
    'P3.P302.DI_Run': '0',
    'P3.MV301.DI_ZSC': '1',
    'P3.MV302.DI_ZSC': '1',
    'P3.MV303.DI_ZSC': '1',
    'P3.MV304.DO_ZSO': '0',
    'P3.MV302.DI_ZSO': '0',
    'P3.MV303.DI_ZSO': '0',
    'P3.MV304.DI_ZSC': '1',
    'P3.MV301.DI_ZSO': '0',
    'P3.P301.DO_Start': '0',
    'P3.P302.DO_Start': '0',
    'P3.MV301.DO_Open': '0',
    'P3.MV302.DO_Open': '0',
    'P3.MV303.DO_Open': '0',
    'P3.MV304.DO_Open': '0',
    'P3.MV301.DO_Close': '0',
    'P3.MV302.DO_Close': '0',
    'P3.MV303.DO_Close': '0',
    'P3.MV304.DO_Close': '0',
    'P4.P401.DI_Run': '0',
    'P4.P401.DO_Start': '0',
    'P4.P402.DI_Run': '0',
    'P4.P402.DO_Start': '0',
    'P5.MV501.DI_ZSO': '0',
    'P5.MV501.DO_Open': '0',
    'P5.MV501.DI_ZSC': '1',
    'P5.MV501.DO_Close': '0',
    'P5.MV502.DI_ZSO': '0',
    'P5.MV502.DO_Open': '0',
    'P5.MV502.DI_ZSC': '1',
    'P5.MV502.DO_Close': '0',
    'P5.MV503.DI_ZSO': '0',
    'P5.MV503.DO_Open': '0',
    'P5.MV503.DI_ZSC': '1',
    'P5.MV503.DO_Close': '0',
    'P5.MV504.DI_ZSO': '0',
    'P5.MV504.DO_Open': '0',
    'P5.MV504.DI_ZSC': '1',
    'P5.MV504.DO_Close': '0',
    'P5.P501.DI_Run': '0',
    'P5.P501_VSD_Out.Start': '0',
    'P5.P502.DI_Run': '0',
    'P5.P501_VSD_Out.Stop': '0',
    'P5.P502_VSD_Out.Start': '0',
    'P5.P502_VSD_Out.Stop': '0',
    'P6.P601.DI_Run': '0',
    'P6.P601.DO_Start': '0',
    'P6.P602.DI_Run': '0',
    'P6.P602.DO_Start': '0'
}

# SPHINX_SWAT_TUTORIAL PLC1 UTILS(
PLC1_ADDR = IP['plc1']
PLC1_TAGS = (
 ('HMI_LIT101_AHH', 1, 'INT'),
 ('HMI_LIT101_Pv', 1, 'INT')
)
PLC1_SERVER = {
    'address': PLC1_ADDR,
    'tags': PLC1_TAGS
}
PLC1_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLC1_SERVER
}
# SPHINX_SWAT_TUTORIAL PLC1 UTILS)

PLCX_ADDR = IP['plcx']
PLCX_TAGS = (
        ('HMI_PLANT_RESET_ON', 2, 'INT'),
        ('HMI_PLANT_AUTO_ON', 2, 'INT'),
        ('HMI_PLANT_AUTO_OFF', 2, 'INT'),
        ('HMI_P2_PERMISSIVE_ON', 2, 'INT'),
        ('HMI_P3_PERMISSIVE_ON', 2, 'INT'),
        ('HMI_P4_PERMISSIVE_ON', 2, 'INT'),
        ('HMI_PLANT_READY', 2, 'INT'),
        ('HMI_MV201_STATUS', 2, 'INT'),
        ('HMI_PLANT_STOP', 2, 'INT'),
        ('HMI_PLANT_START', 2, 'INT'),
        ('HMI_LIT_301_AL', 2, 'INT'),
        ('HMI_LIT_301_AH', 2, 'INT'),
        ('HMI_LIT301_Pv', 2, 'INT'),
        ('HMI_LIT401_Pv', 2, 'INT')
)
PLCX_SERVER = {
    'address': PLCX_ADDR,
    'tags': PLCX_TAGS
}
PLCX_PROTOCOL = {
    'name': 'enip',
    'mode': 1,
    'server': PLCX_SERVER
}


# state {{{1
# SPHINX_SWAT_TUTORIAL STATE(
PATH = 'swat_s1_db.sqlite'
NAME = 'swat_s1'

STATE = {
    'name': NAME,
    'path': PATH
}
# SPHINX_SWAT_TUTORIAL STATE)

SCHEMA = """
CREATE TABLE swat_s1 (
    name              TEXT NOT NULL,
    pid               INTEGER NOT NULL,
    value             TEXT,
    PRIMARY KEY (name, pid)
);
"""

SCHEMA_INIT = """
    INSERT INTO swat_s1 VALUES ('HMI_LIT101_AHH', 1, '0');
    INSERT INTO swat_s1 VALUES ('HMI_LIT101_Pv', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.MV101.DI_ZSO', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.MV101.DI_ZSC', 1, '1');
    INSERT INTO swat_s1 VALUES ('P1.MV101.DO_Open', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.MV101.DO_Close', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.P101.DI_Run', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.P101.DO_Start', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.P102.DI_Run', 1, '0');
    INSERT INTO swat_s1 VALUES ('P1.P102.DO_Start', 1, '0');

    INSERT INTO swat_s1 VALUES ('HMI_PLANT_STOP', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_PLANT_START', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_LIT_301_AL', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_LIT_301_AH', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_PLANT_RESET_ON', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_PLANT_AUTO_ON', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_PLANT_AUTO_OFF', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_P2_PERMISSIVE_ON', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_P3_PERMISSIVE_ON', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_P4_PERMISSIVE_ON', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_PLANT_READY', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_MV201_STATUS', 2, '1');
    INSERT INTO swat_s1 VALUES ('HMI_LIT301_Pv', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_LIT401_Pv', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_LSH601_Alarm', 2, '0');
    INSERT INTO swat_s1 VALUES ('HMI_LSL601_Alarm', 2, '0');
    INSERT INTO swat_s1 VALUES ('P2.MV201.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P2.MV201.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P2.MV201.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P2.MV201.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.P301.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.P302.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV301.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P3.MV302.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P3.MV303.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P3.MV304.DO_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV304.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV302.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV303.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV304.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P3.MV301.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.P301.DO_Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.P302.DO_Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV301.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV302.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV303.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV304.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV301.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV302.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV303.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P3.MV304.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P4.P401.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P4.P401.DO_Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P4.P402.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P4.P402.DO_Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV501.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV501.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV501.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P5.MV501.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV502.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV502.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV502.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P5.MV502.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV503.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV503.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV503.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P5.MV503.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV504.DI_ZSO', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV504.DO_Open', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.MV504.DI_ZSC', 2, '1');
    INSERT INTO swat_s1 VALUES ('P5.MV504.DO_Close', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P501.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P501_VSD_Out.Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P502.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P501_VSD_Out.Stop', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P502_VSD_Out.Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P5.P502_VSD_Out.Stop', 2, '0');
    INSERT INTO swat_s1 VALUES ('P6.P601.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P6.P601.DO_Start', 2, '0');
    INSERT INTO swat_s1 VALUES ('P6.P602.DI_Run', 2, '0');
    INSERT INTO swat_s1 VALUES ('P6.P602.DO_Start', 2, '0')

"""
