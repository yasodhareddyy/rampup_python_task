import re

# Read the text document (replace 'email_txt.txt' with your file path)
with open('email_txt', 'r') as file:
    text = file.read()

# Regular expression pattern to match email addresses
email_pattern = r'[A-Za-z0-9._]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

# Find all email addresses in the text
email_addresses = re.findall(email_pattern, text)


# Print the extracted email addresses
for email in email_addresses:
    print(email)
