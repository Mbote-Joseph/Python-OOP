# Defining the function findMax which finds the maximum grade in a given list.
def findMax(arr):
     
     
    #Initialize max with first element of list of grade.    
    max = arr[0];    
     
    #Loop through the grade list from the first to the last element    
    for i in range(0, len(arr)):    
        #Compare each element of grade list array with max , that was declared earlier   
        if(arr[i] > max):
            #If the grade is greater the maximum grade that was assigned, the new grade value becomes the new maximum value
            max = arr[i];   
             
    # The function returns the value of the maximum value.
    return max

# The list of grades
gradeList = [25, 11, 7, 87, 56,47,12,99,35,78,25];     

# Printing the maximum grade in the given list
print("The maximum grade in a given list is : " + str(findMax(gradeList)));   