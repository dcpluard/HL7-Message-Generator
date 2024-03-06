from hl7apy.core import Segment, Group
import random
from faker import Faker
from datetime import datetime
from utilities import generate_hospital_name, generate_npi, get_admit_date_time, generate_appointment_reason, generate_scheduling_staff, get_appointment_date_time, get_insurance_data

fake = Faker()

# Function called by message_generation.py to generate data and create MSH segment 
def generate_msh_segment(hl7_version, message_type, event_type):
    sending_application = "CLIENTADT"
    sending_facility = "CLIENTFACILITY"
    receiving_application = "INTELY"
    receiving_facility = "INTELY"
    msg_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
    
    msh = Segment('MSH', version=hl7_version)

    msh.msh_3 = sending_application
    msh.msh_4 = sending_facility
    msh.msh_5 = receiving_application
    msh.msh_6 = receiving_facility
    msh.msh_7 = msg_datetime  # Message date/time in YYYYMMDDHHMMSS format
    msh.msh_9 = message_type + "^" + event_type  # Message type
    msh.msh_10 = "123456"  # Message control ID
    msh.msh_11 = "P"  # Processing ID
    msh.msh_12 = hl7_version  # Version ID

    return msh

# Function called by message_generation.py to generate data and create PID segment 
def generate_pid_segment(hl7_version):
    gender_picker = random.randint(1,2)
    pid = Segment('PID', version=hl7_version)
    pid.pid_3 = "MRN" + str(random.randint(100000,999999))  # Patient ID

    if gender_picker == 1:
        patient_first_name = fake.first_name_female() # Patient last name
        pid.pid_8 = 'F' # patient gender
    else:
        patient_first_name = fake.first_name_male() # Patient last name
        pid.pid_8 = 'M' # patient gender

    patient_last_name = fake.last_name() # patient first name
    pid.pid_5.pid_5_1 = patient_last_name
    pid.pid_5.pid_5_2 = patient_first_name
    pid.pid_7 = str(fake.date_of_birth().strftime("%Y%m%d")) # patient DOB
    pid.pid_11.pid_11_1 = fake.street_address() #patient address - street address
    pid.pid_11.pid_11_3 = fake.city() #patient address - city
    pid.pid_11.pid_11_4 = fake.state() #patient address - state
    pid.pid_11.pid_11_5 = str(fake.zipcode()) # patient address - zipcode
    pid.pid_13.pid_13_1 = str(random.randint(201,905)) + "-" + str(random.randint(201,905)) + "-" + str(random.randint(1001,9999)) # patient home phone number
    pid.pid_13.pid_13_4 = patient_first_name.lower() + "." + patient_last_name.lower() + "@gmail.com" # patient email # patient email
    pid.pid_18 = "ACCT" + str(random.randint(100000,999999)) # patient account number
    pid.pid_19 = fake.ssn() # patient SSN

    return pid, patient_last_name, patient_first_name

# Function called by message_generation.py to generate data and create PV1 segment 
def generate_pv1_segment(hl7_version, event_type):
    pv1 = Segment('PV1', version=hl7_version)
    pv1.pv1_2 = "I"  # Patient class (I = Inpatient)
    pv1.pv1_3.pv1_3_2 = str(random.randint(101,701))  # Assigned patient location - room
    pv1.pv1_3.pv1_3_3 = "1"  # Assigned patient location - bed
    pv1.pv1_3.pv1_3_4 = generate_hospital_name()  # Assigned patient location - facility
    pv1.pv1_3.pv1_3_7 = "MAIN"  # Assigned patient location - building
    pv1.pv1_3.pv1_3_8 = str(random.randint(1,7))  # Assigned patient location - floor
    pv1.pv1_7.pv1_7_1 = generate_npi()  # Attending Doctor - ID Number
    pv1.pv1_7.pv1_7_2 = "Physician"  # Attending Doctor - Last Name
    pv1.pv1_7.pv1_7_3 = "Attending"  # Attending Doctor - First Name
    pv1.pv1_7.pv1_7_7 = "MD"  # Attending Doctor - Degree
    pv1.pv1_8.pv1_8_1 = generate_npi()  # Referring Doctor - ID Number
    pv1.pv1_8.pv1_8_2 = "Physician"  #  Referring Doctor - Last Name
    pv1.pv1_8.pv1_8_3 = "Referring"  #  Referring Doctor - First Name
    pv1.pv1_8.pv1_8_7 = "MD"  #  Referring Doctor - Degree
    pv1.pv1_9.pv1_9_1 = generate_npi()  # Consulting Doctor - ID Number
    pv1.pv1_9.pv1_9_2 = "Physician"  #  Consulting Doctor - Last Name
    pv1.pv1_9.pv1_9_3 = "Consulting"  #  Consulting Doctor - First Name
    pv1.pv1_9.pv1_9_7 = "MD"  #  Consulting Doctor - Degree
    pv1.pv1_17.pv1_17_1 = generate_npi() # Admitting Doctor - ID Number
    pv1.pv1_17.pv1_17_2 = "Physician"  #  Admitting Doctor - Last Name
    pv1.pv1_17.pv1_17_3 = "Admitting"  #  Admitting Doctor - First Name
    pv1.pv1_17.pv1_17_7 = "MD"  #  Admitting Doctor - Degree
    pv1.pv1_18 = "I"  # Patient type (O = Outpatient)
    pv1.pv1_19.pv1_19_1 = "FIN" + str(random.randint(1,999999999))  # Visit Number
    admit_date, disch_date = get_admit_date_time()
    pv1.pv1_44.pv1_44_1 = admit_date #Admit Date & Time
    if event_type == 'A03':
        pv1.pv1_45.pv1_45_1 = disch_date #Discharge Date & Time
    else:
        pv1.pv1_45.pv1_45_1 = '' #Discharge Date & Time

    return pv1

# Function called by message_generation.py to generate data and create SCH segment 
def generate_sch_segment(hl7_version):
    sch = Segment('SCH', version=hl7_version)
    sch.sch_1 = "PL-APPT" + str(random.randint(100000,999999)) # Placer Appt ID
    sch.sch_2 = "FL-APPT" + str(random.randint(100000,999999)) # Filler Appt ID
    event_reason, appt_reason = generate_appointment_reason()
    sch.sch_6 = event_reason # Event Reason
    sch.sch_7 = appt_reason # Appointment Reason

    appt_start_time, appt_end_time, appt_duration = get_appointment_date_time()
    sch.sch_9 = str(appt_duration)
    sch.sch_10 = 'MINUTES'
    sch.sch_11.sch_11_4 = appt_start_time
    sch.sch_11.sch_11_5 = appt_end_time

    emp_id, first_name, last_name = generate_scheduling_staff()
    sch.sch_16.sch_16_1 = emp_id
    sch.sch_16.sch_16_2 = first_name
    sch.sch_16.sch_16_3 = last_name
    sch.sch_20.sch_20_1 = emp_id
    sch.sch_20.sch_20_2 = first_name
    sch.sch_20.sch_20_3 = last_name

    return sch

# Function called by message_generation.py to generate data and create IN1 segment 
def generate_in1_segment(hl7_version, patient_last_name, patient_first_name):
    in1 = Segment('IN1', version=hl7_version)
    in1.in1_1 = '1' ## SET ID
    payer_name, payer_id = get_insurance_data()
    in1.in1_2 = payer_id ## Health Plan ID
    in1.in1_3 = payer_id ## Payer ID
    in1.in1_4 = payer_name ## Payer Name
    in1.in1_16.in1_16_1 = patient_last_name
    in1.in1_16.in1_16_2 = patient_first_name

    return in1

# Function called by message_generation.py to generate data and create RGS segment group
def generate_rgs_segment(hl7_version):
    rgs = Segment('RGS', version=hl7_version)
    rgs.rgs_1 = '1' ## Set ID

    return rgs

# Function called by message_generation.py to generate data and create AIS segment 
def generate_ais_segment(hl7_version):
    ais = Segment('AIS', version=hl7_version)
    ais.ais_1 = '1' ## Set ID

    return ais

# Function called by message_generation.py to generate data and create AIG segment 
def generate_aig_segment(hl7_version):
    aig = Segment('AIG', version=hl7_version)
    aig.aig_1 = '1' ## Set ID

    return aig

# Function called by message_generation.py to generate data and create AIL segment 
def generate_ail_segment(hl7_version):
    ail = Segment('AIL', version=hl7_version)
    ail.ail_1 = '1' ## Set ID

    return ail
