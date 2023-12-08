condition_1_false = False
condition_1_true = True
condition_2_false = False
condition_2_true = True

# Outputs True
false_or_true = condition_1_false or condition_2_true
print("\n false_or_true:\n", false_or_true)

# Outputs False
false_or_false = condition_1_false or condition_2_false
print("\n false_or_false:\n", false_or_false)

# Outputs True
true_or_true = condition_1_true or condition_2_true
print("\n true_or_true:\n", true_or_true)


# Outputs False
false_and_true = condition_1_false and condition_2_true
print("\n false_and_true:\n", false_and_true)

# Outputs False
false_and_false = condition_1_false and condition_2_false
print("\n false_and_false:\n", false_and_false)

# Outputs True
true_and_true = condition_1_true and condition_2_true
print("\n true_and_true:\n", true_and_true)