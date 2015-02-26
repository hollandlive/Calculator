def func(x): 
    func = -5*x**5 + 69*x**2 - 47
    return func
print func(0)
print func(1)
print func(2)
print func(3)
####
def fv(pv, ar, py, y):
    rp = ar/py
    p = py * y
    r = p * rp
   
    fv = pv * ((1 + ar) ** p)
    return fv
   
print fv(1000, .02, 365, 3)
print ''
pv = 500
ar = 0.04
p = 10
print (fv == pv * ((1 + ar) ** p))