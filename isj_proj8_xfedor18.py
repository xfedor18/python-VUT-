def e(a = 5, b = {'a':0}):
    b['a'] += 1
    return a + b['a'];
print(e()+e())