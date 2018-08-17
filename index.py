print ('Adding One')

def adding_one(*array):

	# Set i equal to last index in array by default
	i = array[1] if len(array) > 1 else len(array[0]) - 1
	
	# Add one to last digit in array if it is less than nine
	if array[0][i] < 9:
		array[0][i] += 1

		return array[0]

	array[0][i] = 0

	i -= 1	


	return array[0], i


print(adding_one([1, 3, 7, 9]))