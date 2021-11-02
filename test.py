import sys
#function to printMatrix matrix
def printMatrix(matrix,rows,columns):
   for i in range(rows):
       for j in range(columns):
           print(matrix[i][j],end=" ")
       print("\n")

#function to calculate the sum
def sum(matrix,rows,columns):
   sumVal = 0
   for i in range(rows):
       for j in range(columns):
           sumVal += matrix[i][j]
       return sumVal

#function to to print reverse order of matrix
def reverseOrder(matrix,rows,columns):
   for i in range(rows):
       for j in range(columns):
           print(matrix[j][i],end=" ")
       print("\n")

#function to search element in matrix
def search(matrix,rows,columns):
   searchVal = int(input("\nEnter a item to search: "))
   for i in range(rows):
       for j in range(columns):
           if(searchVal == matrix[i][j]):
               print(searchVal,"is found")
               return
   print(searchVal,"is not found")

#function to write matrix in file   
def writeFile(matrix):
   file = open("myListItems.txt","w")
   for i in range(rows):
       for j in range(columns):
           file.write(str(matrix[i][j]))
           file.write(" ")
       file.write("\n")
   print("\nSuccessfully written in file")
   file.close()

#taking the no.of rows from user
rows = int(input("Enter no.of rows: "))
#taking the no.of columns from user
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

print("Entered Matrix")
printMatrix(matrix,rows,columns)
print("Sum of all elements in array",sum(matrix,rows,columns))
print("Reverse order of Matrix")
reverseOrder(matrix,rows,columns)
search(matrix,rows,columns)
writeFile(matrix)