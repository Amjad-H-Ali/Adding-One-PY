print ('Adding One')

def adding_one(*array):

	# Set i equal to last index in array by default
	i = array[1] if len(array) > 1 else len(array[0]) - 1
	
	# If i is less than 0, then all the digits were nines
	# So we have to shift all digits to the right of array and place 1 at index 0
	if i < 0:
		array[0].insert(0, 1)
		return array[0]


	# Add one to last digit in array if it is less than nine
	if array[0][i] < 9:
		array[0][i] += 1

		return array[0]

	# If last digit is nine, set it equal to 0 and decrement i
	array[0][i] = 0
	i -= 1

	# Repeat the process with recursion to carry the one
	return adding_one(array[0], i)






	


print(adding_one([9, 9, 9, 9])) # 10,000

print(adding_one([0])) # 1

print(adding_one([1, 0, 0])) # 101

print(adding_one([1, 2, 3, 4])) # 1,235

