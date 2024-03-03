# Loop two lists in parallel using zip function
# Prerequisite is having two lists with the same length
# Otherwise it will stop with the shorter list

numbers = [1,2,3]
pronounciations = ["one", "two", "three"]
for number, pronounciation in zip(numbers, pronounciations):
    print(number, pronounciation)
    
# POTENTIAL EDGE CASES HERE