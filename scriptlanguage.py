def load_a_list_of_ints():
    
    L = list()
    n = int(input("The number of list elements: "))
    for k in range(n):
        L.append(int(input(str(k+1) + ". element: ")))
    return L
     
def even_indices(L,a,b):
    
    import numpy as np
    numpy_array = np.array(L)
    result =  numpy_array[(numpy_array >= a) & (numpy_array <= b)]
    return result
    
def is_sorted(L):
    
    if(all(L[i] <= L[i + 1] for i in range(len(L)-1))):
        return True
    else:
        return False
    

x=load_a_list_of_ints()
if is_sorted(x):
    print("The list is sorted in ascending order.")
else:
    print("The list is NOT sorted in ascending order.")
    
a=int(input("a= "))
b=int(input("b= "))
print("The result: ", even_indices(x,a,b))
