def log_entries_with_keyword(log_file, keyword):
    try:
        with open(log_file, 'r') as file:

            for line in file:
                log_entry = []
                log_entry.append(line)
                if keyword in line:
                    yield ''.join(log_entry)


    except FileNotFoundError:
        print(f"File '{log_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
log_file = 'data_log.log'  # Replace with the path to your log file
keyword = 'ERROR'  # Replace with your desired keyword

for entry in log_entries_with_keyword(log_file, keyword):
    print(entry)
