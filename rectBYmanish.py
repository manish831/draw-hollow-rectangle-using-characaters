row = int(input("Plz Enter no. of Rows: "))
column = int(input("Plz Enter no. of columns: "))
for i in range(row):
    for j in range(column):
        if i==0 or i == (row-1) or j == 0 or j == (column-1):
            print("*", end=" ")
        else:
            print(" ",end=" ")
    print()                
