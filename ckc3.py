#row num
rows = 5
#num to be printed
b = 1
s = ""
spaces = 5
for i in range(rows,0,-1):    
    
    for j in range(0,i):        
        print(b,end=" ")
    
    
    print( "\r")
    b+=1

