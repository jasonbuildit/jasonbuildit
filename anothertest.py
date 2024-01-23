#
import re

def validate_email(email):
    # Define a regular expression to match a valid email address
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # Compile the regular expression
    email_regex = re.compile(pattern)

    # Use the search method to check if the email address matches the pattern
    match = email_regex.search(email)

    # If a match is found, return True; otherwise, return False
    if match:
        return True
    else:
        return False