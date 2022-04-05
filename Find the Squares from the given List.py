sample_list = [4, 5, 2, 9]
print("Original list: ", sample_list)
result = map(lambda x: x * x, sample_list) 
print("\nSquare the elements of the list:")
print(list(result))