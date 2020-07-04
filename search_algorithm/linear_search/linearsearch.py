#function
def linear_search(array,element):
    #finding the length of the array
    n = len(array)
    for i in range(0,n):
        if array[i] == element:
            return i
        
    return -1
            





#driver code
#array to search
array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

#element to find, expected result = 6
element = 5

#printing the index value
print(linear_search(array,element))


