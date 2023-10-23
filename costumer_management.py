import json
import os


def customer_load(customer_number):
    file_path = os.path.join('data', 'customers', f"{customer_number}.json")

    try:
        with open(file_path, 'r') as file:
            customer_data = json.load(file)
            return customer_data
    except FileNotFoundError:
        return None



def customer_edit(customer_id, data_name, new_value):
    # Define the path to the "data/customers" folder
    data_folder = os.path.join(os.path.dirname(__file__), 'data', 'customers')

    # Construct the JSON file path based on the customer ID
    json_file_path = os.path.join(data_folder, f'customer{customer_id}.json')

    if os.path.exists(json_file_path):
        # Load existing customer data from the JSON file
        with open(json_file_path, 'r') as f:
            customer_data = json.load(f)

        # Update specific data field with new value
        if data_name in customer_data:
            customer_data[data_name] = new_value

            # Save updated customer data back to the JSON file
            with open(json_file_path, 'w') as f:
                json.dump(customer_data, f, indent=4)
        else:
            raise ValueError(f"Data field '{data_name}' not found in customer data.")
    else:
        raise FileNotFoundError(f"Customer {customer_id} not found.")


def customer_refresh():
    # Define the path to the "data/customers" folder
    data_folder = os.path.join(os.path.dirname(__file__), 'data', 'customers')

    # Check if the folder exists
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)  # Create the folder if it doesn't exist

    # Get a list of JSON files in the folder
    json_files = [file for file in os.listdir(data_folder) if file.endswith('.json')]

    # Extract customer IDs from JSON filenames
    customer_ids = [json_file.split("customer")[0].split(".json")[0] for json_file in json_files]

    return customer_ids


def get_next_customer_number():
    # Define the path to the "data/customers" folder
    data_folder = os.path.join(os.path.dirname(__file__), 'data', 'customers')

    # Get the list of files in the folder with '.json' extension
    json_files = [file for file in os.listdir(data_folder) if file.endswith('.json')]

    # Calculate the next customer number
    next_customer_number = len(json_files) + 1
    print("Key=" + str(next_customer_number))
    return next_customer_number  # Format as '0001', '0002', etc.


def customer_new(customer_name, customer_phone, customer_mobile, last_sessions, employee_name, treatment):
    # Define the path to the "data/customers" folder
    data_folder = os.path.join(os.path.dirname(__file__), 'data', 'customers')

    # Check if the folder exists
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)  # Create the folder if it doesn't exist

    # Get the next available customer number
    customer_number = get_next_customer_number()
    if customer_number is None:
        raise Exception("No available customer numbers.")

    # Construct the JSON file path based on the customer number
    json_file_path = os.path.join(data_folder, f'{customer_number}.json')

    # Create customer data dictionary
    customer_data = {
        "Customer_Name": customer_name,
        "Customer_Phone": customer_phone,
        "Customer_Mobile": customer_mobile,
        "Last_Sessions": last_sessions,
        "Employee_Name": employee_name,
        "Treatment": treatment,
        "Customer_Number": customer_number
    }

    # Write customer data to JSON file
    with open(json_file_path, 'w') as f:
        json.dump(customer_data, f, indent=4)