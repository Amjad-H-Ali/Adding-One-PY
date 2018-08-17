print ('Adding One')

def adding_one(*array):

	i = array[1] if len(array) > 1 else len(array[0]) - 1
	
	print (i)


adding_one([1, 3, 7, 2])