
# Name: Alzaid khan DIV: E(ECS)
# UIN: 241S009  Roll no. 09

import re

# Function to validate phone number
def validate_phone(phone):
    # Regex pattern for phone number (example format: 123-456-7890 or (123) 456-7890)
    phone_pattern = r'^\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    if re.match(phone_pattern, phone):
        return True
    else:
        return False

# Function to validate email address
def validate_email(email):
    # Regex pattern for email (standard email format)
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_pattern, email):
        return True
    else:
        return False

# Input phone number and email address
phone = input("Enter your phone number: ")
email = input("Enter your email ID: ")

# Validate inputs
if validate_phone(phone):
    print("Phone number is valid.")
else:
    print("Invalid phone number format.")

if validate_email(email):
    print("Email ID is valid.")
else:
    print("Invalid email address format.")
