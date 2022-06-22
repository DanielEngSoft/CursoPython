def testar(a, b):
    ma = a
    if ma < b:
        ma = b
    me = b
    if me > b:
        me = b
    resultado = ma % me
    if resultado == 0:
        return me
    else:
        testar(me, ma)


print(testar(120, 30))
