import re

# Read the content from the "urls_data" file
url_pattern=r'((https:|http:)//(www|\w+)|www)\.([a-zA-Z0-9]+\.(com|in|org)|[a-zA-Z0-9]+)$'
with open("urls_data", "r") as file:
    for line in file:

        out=re.search(url_pattern,line)
        if out:
            print(out.group())

