num1 = [1, 2, 3, 4, 5, 6, 7] 
print("Original num list: ", num1)
result = map(lambda x: x + x + x, num1) 
print("\nTriple of list numbers:")
print(list(result))