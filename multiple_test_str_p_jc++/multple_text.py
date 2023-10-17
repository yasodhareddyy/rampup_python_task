import re

# Your multiline text string containing code blocks
code_string = """
def add(a, b):
    return a + b

public int multiply(int x, int y) {
    return x * y;
}

void printMessage(String message) {
    System.out.println(message);
}
"""

# Define a regular expression pattern to match function declarations
pattern = r'(?:(?:def|public|private|protected|static|void)\s+)?\w+\s+(\w+)\s*\((.*?)\)'

# Find all matches in the code string
matches = re.findall(pattern, code_string, re.MULTILINE)

# Iterate through the matches and print function names and parameters
for match in matches:
    function_name = match[0]
    parameters = match[1].split(',')
    parameters = [param.strip() for param in parameters]
    print(f"Function Name: {function_name}")
    print(f"Parameters: {', '.join(parameters)}")
    print()
