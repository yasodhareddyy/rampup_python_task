import re


# Function to extract sequences from a given paragraph
def extract_sequences(paragraph):
    # Define a regular expression pattern to match "Start: ... End:"
    pattern = r'Start:(.*?)End:'

    # Use re.findall to find all matching sequences in the paragraph
    sequences = re.findall(pattern, paragraph, re.DOTALL)

    return sequences


# Read the text document
with open('sample', 'r') as file:
    # Read the content of the document
    document_content = file.read()

    # Split the document into paragraphs (assuming paragraphs are separated by '\n\n')
    paragraphs = document_content.split('\n\n')

    # Iterate through each paragraph and extract sequences
    for i, paragraph in enumerate(paragraphs):
        sequences = extract_sequences(paragraph)

        # Print the sequences found in this paragraph
        for j, sequence in enumerate(sequences):
            print(f"Paragraph {i + 1}, Sequence {j + 1}: {sequence.strip()}\n")
