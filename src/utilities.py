import random
from faker import Faker
from datetime import datetime, timedelta
from reference_data import insurances

fake = Faker()

def generate_hospital_name():
    hospital_prefixes = ['Saint', 'Mercy', 'Mount', 'Memorial', 'General']
    hospital_suffixes = ['Hospital', 'Medical Center', 'Clinic', 'Health System', 'Healthcare']

    prefix = random.choice(hospital_prefixes)
    middle = fake.city()
    suffix = random.choice(hospital_suffixes)

    return f"{prefix} {middle} {suffix}"

def generate_npi():
    # Generate the first 9 digits randomly
    npi = [random.randint(0, 9) for _ in range(9)]
    
    # # Prepend the NPI prefix for a 10-digit NPI (80840 for individual providers)
    # npi = [8, 0, 8, 4, 0] + npi
    
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

def generate_appointment_reason():
    reasons = [
        "CHECK-UP",
        "EMERGENCY",
        "FOLLOW-UP",
        "ROUTINE",
        "WALK-IN"
    ]
    event_reason = appt_reason = random.choice(reasons)
    return event_reason, appt_reason

def generate_scheduling_staff():
    emp_id = str(random.randint(100000,999999)) # Employee Nbr
    first_name = fake.first_name()
    last_name = fake.last_name()
    return emp_id, first_name, last_name

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

def get_insurance_data():
    insurance = random.choice(insurances)
    payer_name = insurance['payer_name']
    payer_id = insurance['payer_id']

    return payer_name, payer_id


