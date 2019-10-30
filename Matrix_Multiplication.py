#MATRIX A

rows1=int(input("Enter The Number of Rows For A: "))
cols1=int(input("Enter The Number of Columns For A: "))
arr=[[0 for i in range(cols1)]for j in range(rows1)]
print("Enter The Matrix A Data :")
for r in range(rows1):
    for c in range(cols1) :
        print("Enter the value for [",r,"]","[",c,"]",end=" :")
        arr[r][c]=int(input(""))
        
#MATRIX B
        
rows2=int(input("Enter The Number of Rows For B: "))
cols2=int(input("Enter The Number of Columns For B: "))
brr=[[0 for i in range(cols2)]for j in range(rows2)]
print("Enter The Matrix B Data :")
for r in range(rows2):
    for c in range(cols2) :
        print("Enter the value for [",r,"]","[",c,"]",end=" :")
        brr[r][c]=int(input(""))
        
#printing A & B
        
print("Matrix A :")
for row in arr:
    print("\t\t",row)
print("Matrix B :")
for row in brr:
    print("\t\t",row)
    
#MATRIX C(Multi_answer)

if(cols1 != rows2):
    print("Cannot Multiply A & B ---------INVALID NUMBER OF ROWS AND COLUMNS")
else:
    crr=[[0 for i in range(cols2)]for j in range(rows1)]
    print("Multiplying The Matrix A and B")
                #Algo Of Mat-Mul 3 Nested-For-Loops
    for r in range(rows1):
        for c in range(cols2):
            for k in range(cols1):
                crr[r][c]+=arr[r][k]*brr[k][c]
    
    print("Answer of A X B:")
    for row in crr:
        
          print("\t\t",row)
  




