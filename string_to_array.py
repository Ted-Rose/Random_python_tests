string = 'key="1111",ballon="22222",funny="333",dog="444",fast="555"'

# Split the string by commas
pairs = string.split(',')

# Create an empty dictionary
associative_array = {}

# Iterate over the pairs and split each pair into key and value
for pair in pairs:
    # Split each pair by the equal sign
    key, value = pair.split('=')

    # Remove any surrounding whitespace and double quotes from the key and value
    key = key.strip().strip('"')
    value = value.strip().strip('"')

    # Add the key-value pair to the dictionary
    associative_array[key] = value

# Print the resulting associative array
print(associative_array["key"])

