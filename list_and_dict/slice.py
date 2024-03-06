sample_list = [1,2,3,4,5,6,7,8]
start = 2
end = 5
slice_example = sample_list[start:end]  # Default 0 and len-1 if not specified -> Intuinitive thinking
# If specify negative index => Starts from end
print(sample_list[-3:-1])
step = 2  # Default 1
print(sample_list[::step])  # Apply the same logic
# AVOID to specify ALL start, end, step AND use negative index since it is very hard to comprehend