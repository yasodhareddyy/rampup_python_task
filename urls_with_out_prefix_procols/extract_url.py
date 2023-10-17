import re

# Define the regular expression pattern to find URLs
url_pattern = r'((https:|http:)//(www|\w+)|www)\.([a-zA-Z0-9]+\.(com|in|org)|[a-zA-Z0-9]+)$'

# Open and read the content from the "urls_data" file
with open("urls_data", "r") as file:
    for line in file:
        # Search for the URL pattern in each line of the file
        match = re.search(url_pattern, line)
        if match:
            # If a match is found, print the matched URL
            print(match.group())
