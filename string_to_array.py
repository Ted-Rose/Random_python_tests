string = 'keyId="1111=",baloon="22222===",funyy="333",dog="444",lol="555"'


# Split the string by commas
pairs = string.split(',')

# Create an empty dictionary
associative_array = {}

# Iterate over the pairs and split each pair into key and value
for pair in pairs:
    # Split each pair by the equal sign, only at the first occurrence
    split_pair = pair.split('=', 1)

    # Remove any surrounding whitespace and double quotes from the key
    key = split_pair[0].strip().strip('"')

    # If the split resulted in two parts, assign the second part as the value
    if len(split_pair) == 2:
        value = split_pair[1].strip().strip('"')
    else:
        value = ""

    # Add the key-value pair to the dictionary
    associative_array[key] = value

# Print the resulting associative array
print(associative_array)
