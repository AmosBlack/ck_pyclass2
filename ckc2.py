#row num
rows = 5
#num to be printed
b = '+'
s = ""
spaces = 5
for i in range(0,rows):
    
    for k in range(0,spaces ):
        print(s,end = " ")
    for j in range(0,i+1):        
        print(b,end=" ")
    spaces -= 1
    
    print( "\r")

