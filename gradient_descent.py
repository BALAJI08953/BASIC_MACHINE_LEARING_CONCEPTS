import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
xs=[1,2,3,4,5]
ys=[2.9,5.2,7.1,8.8,11.1]
def loss(w,b):
    err=0
    for x,y in zip(xs,ys):
        err+=(w*x+b-y)**2
    return err/len(xs)
def slope(w,b,h=1e-6):
    dw=(loss(w+h,b)-loss(w,b))/h
    db=(loss(w,b+h)-loss(w,b))/h
    return dw,db
w,b,rate=0.0,0.0,0.05
for step in range (300):
    dw,db=slope(w,b)
    w,b=w-rate*dw,b-rate*db
print(round(w,2),round(b,2),loss(w,b))
plt.bar(round(w,2),round(b,2),loss(w,b))
plt.show()