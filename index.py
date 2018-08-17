print ('Adding One')

def adding_one(*array):

	i = array[1] if len(array) > 1 else len(array[0]) - 1
	

	if array[0][i] < 9:
		array[0][i] += 1

		return array[0]

	return i


print(adding_one([1, 3, 7, 2]))