import csv
from faker import Faker
import random
from google.cloud import storage

# Initialize Faker
fake = Faker()

# File to save
file_name = "employee_data.csv"

# GCS bucket details
bucket_name = "employee-data-storage-bucket" 
destination_blob_name = "employee_data.csv"  # File name in GCS

# Function to generate employee data
def generate_employee_data(num_employees):
    columns = [
        "Employee ID", "Name", "Email", "Phone Number", "Address",
        "Date of Birth", "Job Title", "Department", "Joining Date", "Salary", "Password"
    ]
    
    job_categories = {
        "Administration": ["HR Manager", "Office Administrator", "Executive Assistant"],
        "Technical": ["Software Engineer", "Data Analyst", "System Administrator"],
        "Sales": ["Sales Manager", "Account Executive", "Marketing Specialist"],
        "Support": ["Customer Support", "Technical Support Specialist", "Helpdesk Technician"]
    }
    
    departments = {
        "Administration": "HR",
        "Technical": "Engineering",
        "Sales": "Sales",
        "Support": "Support"
    }
    
    data = []

    for _ in range(num_employees):
        try:
            employee_id = fake.unique.random_int(min=1000, max=9999)
            name = fake.name()
            email = fake.email()
            phone = fake.phone_number()
            address = fake.address().replace("\n", ", ")  # Flatten multi-line addresses
            dob = fake.date_of_birth(minimum_age=22, maximum_age=65).strftime("%Y-%m-%d")
            job_category = random.choice(list(job_categories.keys()))
            job_title = random.choice(job_categories[job_category])
            department = departments[job_category]
            joining_date = fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
            salary = round(random.uniform(30000, 150000), 2)
            password = fake.password()

            row = [
                employee_id, name, email, phone, address,
                dob, job_title, department, joining_date, salary, password
            ]
            
            # Ensure no empty fields
            if len(row) == len(columns) and all(row):
                data.append(row)
            else:
                print(f"Skipped row due to missing data: {row}")
        except Exception as e:
            print(f"Error generating row: {e}")

    # Save to CSV
    with open(file_name, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)

    print(f"Data successfully written to {file_name}")

# Function to upload file to GCS bucket
def upload_to_gcs(local_file, bucket_name, destination_blob_name):
    try:
        # Initialize a client
        storage_client = storage.Client()
        # Get the bucket
        bucket = storage_client.bucket(bucket_name)
        # Create a new blob and upload the file
        blob = bucket.blob(destination_blob_name)
        blob.upload_from_filename(local_file)
        print(f"File {local_file} uploaded to {bucket_name}/{destination_blob_name}.")
    except Exception as e:
        print(f"Failed to upload to GCS: {e}")

# Main function
if __name__ == "__main__":
    # Generate data for 1000 employees
    generate_employee_data(1000)
    
    # Upload the file to GCS bucket
    upload_to_gcs(file_name, bucket_name, destination_blob_name)
