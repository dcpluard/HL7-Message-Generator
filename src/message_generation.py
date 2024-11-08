from hl7apy.core import Message
from datetime import datetime
from segment_generation import generate_msh_segment, generate_pid_segment, generate_pv1_segment, generate_sch_segment, generate_in1_segment, generate_rgs_segment, generate_ais_segment, generate_aig_segment, generate_ail_segment

## Function to assemble and generate message for ADT A01
def generate_adt_a01(message_type, event_type, hl7_version):
    msg = Message("ADT_A01", version=hl7_version)
    ## MSH
    msh_segment = generate_msh_segment(hl7_version, message_type, event_type, msg)
    #msg.add(msh_segment)
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

## Function to assemble and generate message for ADT A03
def generate_adt_a03(message_type, event_type, hl7_version):
    msg = Message("ADT_A03", version=hl7_version)
    ## MSH
    msh_segment = generate_msh_segment(hl7_version, message_type, event_type, msg)
    #msg.add(msh_segment)
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

## Function to assemble and generate message for SIU S12
def generate_siu_s12(message_type, event_type, hl7_version):
    msg = Message("SIU_S12", version=hl7_version)
    ## MSH
    msh_segment = generate_msh_segment(hl7_version, message_type, event_type, msg)
    #msg.add(msh_segment)
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