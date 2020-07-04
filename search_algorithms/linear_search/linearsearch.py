#linear search is simply searching an array from start to end
#input = [1,5,8,10]; find '8'. Output : 2

def linear_search(element,array):
    n = len(array)
    for i in range(0,n):
        if array[i] is element:
            return i
        else:
            return -1










#input array
array = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]

#element to find , expected output = 6
n = 5

print(linear_search(n,array))

