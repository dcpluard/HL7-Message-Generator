from hl7apy.core import Message
from datetime import datetime
from segment_generation import generate_pid_segment, generate_pv1_segment, generate_sch_segment, generate_in1_segment, generate_rgs_segment, generate_ais_segment, generate_aig_segment, generate_ail_segment

SENDING_APPLICATION = "CLIENTADT"
SENDING_FACILITY = "CLIENTFACILITY"
RECEIVING_FACILITY = "INTELY"
RECEIVING_APPLICATION = "INTELY"
MESSAGE_DATE_TIME = datetime.now().strftime("%Y%m%d%H%M%S")

def generate_adt_a01(message_type, event_type, hl7_version):
    msg = Message("ADT_A01", version=hl7_version)
    ## MSH
    msg.msh.msh_3 = SENDING_APPLICATION
    msg.msh.msh_4 = SENDING_FACILITY
    msg.msh.msh_5 = RECEIVING_APPLICATION
    msg.msh.msh_6 = RECEIVING_FACILITY
    msg.msh.msh_7 = MESSAGE_DATE_TIME  # Message date/time in YYYYMMDDHHMMSS format
    msg.msh.msh_9 = message_type + "^" + event_type  # Message type
    msg.msh.msh_10 = "123456"  # Message control ID
    msg.msh.msh_11 = "P"  # Processing ID
    msg.msh.msh_12 = hl7_version  # Version ID
    ## EVN
    msg.evn.evn_1 = event_type
    ## PID
    pid_segment, patient_last_name, patient_first_name = generate_pid_segment(hl7_version)
    msg.add(pid_segment)
    ## PV1
    pv1_segment = generate_pv1_segment(hl7_version, event_type)
    msg.add(pv1_segment)
    ## IN1
    in1_segment = generate_in1_segment(hl7_version, patient_last_name, patient_first_name)
    msg.add(in1_segment)
    return msg.to_er7().replace('\r', '\n')

def generate_adt_a03(message_type, event_type, hl7_version):
    msg = Message("ADT_A03", version=hl7_version)
    ## MSH
    msg.msh.msh_3 = SENDING_APPLICATION
    msg.msh.msh_4 = SENDING_FACILITY
    msg.msh.msh_5 = RECEIVING_APPLICATION
    msg.msh.msh_6 = RECEIVING_FACILITY
    msg.msh.msh_7 = MESSAGE_DATE_TIME  # Message date/time in YYYYMMDDHHMMSS format
    msg.msh.msh_9 = message_type + "^" + event_type  # Message type
    msg.msh.msh_10 = "123456"  # Message control ID
    msg.msh.msh_11 = "P"  # Processing ID
    msg.msh.msh_12 = hl7_version  # Version ID
    ## EVN
    msg.evn.evn_1 = event_type
    ## PID
    pid_segment, patient_last_name, patient_first_name = generate_pid_segment(hl7_version)
    msg.add(pid_segment)
    ## PV1
    pv1_segment = generate_pv1_segment(hl7_version, event_type)
    msg.add(pv1_segment)
    ## IN1
    in1_segment = generate_in1_segment(hl7_version, patient_last_name, patient_first_name)
    msg.add(in1_segment)
    return msg.to_er7().replace('\r', '\n')

def generate_siu_s12(message_type, event_type, hl7_version):
    msg = Message("SIU_S12", version=hl7_version)
    ## MSH
    msg.msh.msh_3 = SENDING_APPLICATION
    msg.msh.msh_4 = SENDING_FACILITY
    msg.msh.msh_5 = RECEIVING_APPLICATION
    msg.msh.msh_6 = RECEIVING_FACILITY
    msg.msh.msh_7 = MESSAGE_DATE_TIME  # Message date/time in YYYYMMDDHHMMSS format
    msg.msh.msh_9 = message_type + "^" + event_type  # Message type
    msg.msh.msh_10 = "123456"  # Message control ID
    msg.msh.msh_11 = "P"  # Processing ID
    msg.msh.msh_12 = hl7_version  # Version ID
    ## EVN
    msg.evn.evn_1 = event_type
    ## SCH
    sch_segment = generate_sch_segment(hl7_version)
    msg.add(sch_segment)
    ## PID
    pid_segment, patient_last_name, patient_first_name = generate_pid_segment(hl7_version)
    msg.add(pid_segment)
    ## PV1
    pv1_segment = generate_pv1_segment(hl7_version, event_type)
    msg.add(pv1_segment)
    ## IN1
    in1_segment = generate_in1_segment(hl7_version, patient_last_name, patient_first_name)
    msg.add(in1_segment)
    ## RGS
    rgs_segment = generate_rgs_segment(hl7_version)
    msg.add(rgs_segment)
    ## AIS
    ais_segment = generate_ais_segment(hl7_version)
    msg.add(ais_segment)
    ## AIG
    aig_segment = generate_aig_segment(hl7_version)
    msg.add(aig_segment)
    ## AIL
    ail_segment = generate_ail_segment(hl7_version)
    msg.add(ail_segment)
    return msg.to_er7().replace('\r', '\n')