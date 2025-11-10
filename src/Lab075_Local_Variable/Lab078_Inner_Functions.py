def outer_fun():
    var1=10

    def inner_fun():
        var2=20
        print(var1)
    def inner_fun2():
        print(var1)
        #print(var2)

    inner_fun()
    inner_fun2()

outer_fun()