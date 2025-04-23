#17 Write a program that reads a text file containing various data (e.g., names, emails, phone 
numbers). Use regular expressions to extract specific types of data, such as email addresses, phone 
numbers, dates (e.g., MM/DD/YYYY format).
                
# Name: Alzaid khan DIV: E(ECS)
# UIN: 241S009  Roll no. 09

import re

def extract_data(file_path):

    with open(file_path, 'r') as file:
        content = file.read()

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

phone_pattern = r'\b[6-9]\d{9}\b'

date_pattern = r'\b(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/([0-9]{4})\b'

emails = re.findall (email_pattern, content)

phones = re.findall (phone_pattern, content)

dates = re.findall(date_pattern, content)

formatted_dates = ['{}/{}/{}'.format(m, d, y) for m, d , y in dates]

return emails, phones, formatted_dates

file_path = 'data.txt'

emails, phones, dates = extract_data(file_path)

print(" Email Addresses Found:")

print("\n".join(emails) if emails else "None found")

print("\n Phone Numbers Found:")

print("\n".join(phones) if phones else "None found")

print("\n Dates Found (MM/DD/YYYY):")

print("\n".join(dates) if dates else "None found")
