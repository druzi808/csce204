#Author: Drew Rafferty

# 1 2 3
# 2 4 6
# 3 6 9

endNum = int(input("Enter how many multiplication tables: "))

#loop thru rows
for row in range(1, endNum + 1):
    #print(row, end = "")
    #loop thru columns 
    for col in range(1, endNum + 1):
        #if single digit
        if(len(str(row * col)) < 2):
            print(f" {row * col}", end = " ")
        else:
            print(f"{row * col}", end = " ")
          
    print() # display new line