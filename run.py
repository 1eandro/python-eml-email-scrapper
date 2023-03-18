import os
import csv
import email
import re

# Define the root directory where the .eml files are stored
root_dir = '/Users/<your-user>/Library/Application Support/Vivaldi/Default/Mail/<folder>/'



# Create a list to hold the data we want to extract
data = []

# Define a regular expression pattern to match the received date
received_date_pattern = r'[a-zA-Z]{3}, \d{1,2} [a-zA-Z]{3} \d{4} \d{2}:\d{2}:\d{2} [-+]\d{4}'

# Define a function to extract the domain of an email address
def extract_domain(email_address):
    parts = email_address.split('@')
    if len(parts) == 2:
        return parts[1].replace('>','')
    else:
        return None

# Define a function to extract data from a single .eml file
def extract_data(filename):
    with open(filename, 'r', encoding='latin-1') as f:
        msg = email.message_from_file(f)
        
    sender = str(msg['From']).replace('\n', '\\n')
    returnPath = str(msg['Return-Path']).replace('\n', '\\n')
    receivedDate = msg['Received'] if msg['Received'] is not None else 'null'
    domain = extract_domain(sender)
    
    # Extract the received date from the "Received" field using regular expressions
    match = re.search(received_date_pattern, receivedDate)
    if match:
        received_date = str(match.group())
    else:
        received_date = ''

    # Extract the domain of the Sender
    match = re.search(received_date_pattern, receivedDate)
    
    return sender, domain, returnPath, received_date

# Loop through all the subdirectories recursively
for subdir, dirs, files in os.walk(root_dir):
    for filename in files:
        if filename.endswith('.eml'):
            # Extract the data from the .eml file and add it to our list
            filepath = os.path.join(subdir, filename)
            row = extract_data(filepath)
            data.append(row)

# Write the data to a .csv file
with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Sender', 'Domain', 'Return Path', 'Received Date'])
    for row in data:
        writer.writerow(row)
