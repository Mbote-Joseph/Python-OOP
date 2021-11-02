
#function to printMatrix matrix
def printMatrix(matrix,rows,columns):
   for i in range(rows):
       for j in range(columns):
           print(matrix[i][j],end=" ")
       print("\n")

#function to calculate the sum and return the sum value
def sum(matrix,rows,columns):
   sumValue = 0
   for i in range(rows):
       for j in range(columns):
           sumValue += matrix[i][j]
   return sumValue

# average function that returns the average  value of the matrix and returns the average value
def average(matrix, rows, columns):
    # Geting the total number of elements in a matrix
    elements=rows*columns
    # Testing code to see if I can get the average function can get the number of elements in the matrix
    # print(elements)

    # Geting the average value by calling the sum function and dividing by the number of elements
    averageValue= sum(matrix,rows,columns)/elements
    # returning the average value
    return averageValue

#taking the number of rows of the matrix from user
rows = int(input("Enter no.of rows: "))
#taking the number of columns of the matrix from user
columns = int(input("Enter no.of columns: "))
#intilize the matrix
matrix = []
for i in range(rows):
   #creating a empty row
   row = []
   for j in range(columns):
       #entering all elements in row
       row.append(int(input("Enter element : ")))
   #row is adding to matix
   matrix.append(row)


# Testing the sum funtion
# print(sum(matrix,rows,columns))
           

print("Entered Matrix")
# Printing the matrix
printMatrix(matrix,rows,columns)
# Code to test if I can get the sum of all the elements in the matrix
print("Sum of all elements in array",sum(matrix,rows,columns))
# Code to print the average of all the elements in the matrix
print("Average of all elements in array",average(matrix, rows, columns))

