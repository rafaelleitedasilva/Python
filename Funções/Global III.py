X = 10
def incremento():
    global X
    incremento=5 #váriavel local
    X+= incremento #cópia do valorde x
    
incremento()  
print(X)