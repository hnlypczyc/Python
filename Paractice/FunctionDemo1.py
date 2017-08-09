x = " I am Nancy"
def fun():
    x=100
    print(x)
    global y
    y =200
fun()
print(x)
print(y)
