a = 1
def external():
    global a
    a = 200
    print(a)
    b = 100
    def internal():
        nonlocal b
        print (b)
        b = 200
        return b
    internal()
#print (b)

print (external())
