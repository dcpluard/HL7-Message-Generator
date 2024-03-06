from message_generation import generate_adt_a01, generate_adt_a03, generate_siu_s12
import uuid
import os

## Collects user inputs and executes the function to generate meassges
def main():
    message_type = input("Enter Message Type: ")
    event_type = input("Enter Event Type: ")
    output_mode = int(input("Enter Output Mode (1 for console, 2 for directory): "))
    hl7_version = "2.3"
    MESSAGE_ID = uuid.uuid1()

    ## Calls message_generation factory functions to generate messages
    if message_type == "ADT" and event_type == "A01":
        message = generate_adt_a01(message_type, event_type, hl7_version) # function to generate A01
    elif message_type == "ADT" and event_type == "A03":
        message = generate_adt_a03(message_type, event_type, hl7_version) # function to generate A04
    elif message_type == "SIU" and event_type == "S12":
        message = generate_siu_s12(message_type, event_type, hl7_version) # function to generate A04
    else:
        print("Invalid Message Type")
        return
    
    # Use output_mode to either print to console or generate to directory
    if output_mode == 1:
        print(message)
    elif output_mode == 2:
        # create file name for each message
        file_name = str(MESSAGE_ID)

        # define base path
        base_path = "messages"

        # Check if the directory exists, if not, create it
        if not os.path.exists(base_path):
            os.makedirs(base_path)

        # Define the file path and name within the 'messages' folder
        file_path = os.path.join(base_path, f"{file_name}.hl7")

        # write the message to the file
        with open(file_path, "w") as file:
            file.write(message)

        print(f"Message written to {file_path}")

if __name__ == "__main__":
    main()