import random
from faker import Faker
from datetime import datetime, timedelta
from reference_data import insurances, reasons

fake = Faker()

## Utility function to generate a realistic hospital/facility name. 
## This function could also be modified to pull from reference_data
def generate_hospital_name():
    hospital_prefixes = ['Saint', 'Mercy', 'Mount', 'Memorial', 'General']
    hospital_suffixes = ['Hospital', 'Medical Center', 'Clinic', 'Health System', 'Healthcare']

    prefix = random.choice(hospital_prefixes)
    middle = fake.city()
    suffix = random.choice(hospital_suffixes)

    return f"{prefix} {middle} {suffix}"

## Utility function to generate valid provider NPI numbers
def generate_npi():
    # Generate the first 9 digits randomly
    npi = [random.randint(0, 9) for _ in range(9)]
    
    # Calculate the checksum using the Luhn algorithm
    def luhn_checksum(digits):
        total = 0
        for i, digit in enumerate(reversed(digits)):
            if i % 2 == 0:
                total += digit
            else:
                doubled = digit * 2
                total += doubled if doubled < 10 else doubled - 9
        return (10 - (total % 10)) % 10
    
    checksum = luhn_checksum(npi)
    
    # Append the checksum digit to the NPI
    npi.append(checksum)
    
    # Convert the list of digits to a string
    npi_str = ''.join(map(str, npi))
    
    return npi_str

## Utility function to generate random admit and discharge datetime within the last 48 hours. 
## The discharge date will be within 24 hours after the admit date
def get_admit_date_time():
    now = datetime.now()
    random_two_day_delta = timedelta(hours=random.randint(0,48),
                                  minutes=random.randint(0,59),
                                  seconds=random.randint(0,59))
    random_one_day_delta = timedelta(hours=random.randint(0,48),
                                  minutes=random.randint(0,59),
                                  seconds=random.randint(0,59))
    random_admit_date = now - random_two_day_delta
    admit_date = random_admit_date.strftime("%Y%m%d%H%M%S")

    random_disch_date = random_admit_date + random_one_day_delta
    disch_date = random_disch_date.strftime("%Y%m%d%H%M%S")

    return admit_date, disch_date

## Utility function to get appointment reasons from reference data
def generate_appointment_reason():
    event_reason = appt_reason = random.choice(reasons)
    return event_reason, appt_reason

## Utility function to generate a random scheduling staff member
def generate_scheduling_staff():
    emp_id = str(random.randint(100000,999999)) # Employee Nbr
    first_name = fake.first_name()
    last_name = fake.last_name()
    return emp_id, first_name, last_name

## Utility function to get appointment start time for some datetime in the next 30 days
## defines appointment duration and creates the appointment end time
def get_appointment_date_time():
    now = datetime.now()
    random_30_delta = timedelta(days=random.randint(0,30),
                                  hours=random.randint(0,24))
    random_appt_start_time = now + random_30_delta
    appt_duration_slots = [15, 30, 60]
    appt_duration = random.choice(appt_duration_slots)
    random_appt_end_time = random_appt_start_time + timedelta(minutes=appt_duration)
    appt_start_time = random_appt_start_time.strftime("%Y%m%d%H%M%S")
    appt_end_time = random_appt_end_time.strftime("%Y%m%d%H%M%S")

    return appt_start_time, appt_end_time, appt_duration

## Utility function to get insurance/payer from reference data
def get_insurance_data():
    insurance = random.choice(insurances)
    payer_name = insurance['payer_name']
    payer_id = insurance['payer_id']

    return payer_name, payer_id


