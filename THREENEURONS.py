import math
data=[(0,0,0),(0,1,1),(1,0,1),(1,1,0)]
sig=lambda z:1/(1+math.exp(-z))
w=[.3,-.8,.5,-.2,.1,.7,-.6,.2]
lr=0.5
for epoch in range(3000):
    for x0,x1,y in data:
        a=sig(w[0]*x0+w[1]*x1+w[2])
        b=sig(w[3]*x0+w[4]*x1+w[5])
        p=sig(w[6]*a+w[7]*b+w[8])
        err=p-y
        ga=err*w[6]*a*(1-a)
        gb=err*w[7]*b*(1-b)
        grad=[ga*x0,ga*x1,ga,gb*x0,gb*x1,gb,err*a,err*b,err]
        for i in range(9):w[i]-=lr*grad[i]
print("\nFinal weights:")
print(w)

print("\nFinal predictions:")

for x0,x1,y in data:

    a = sig(w[0]*x0 + w[1]*x1 + w[2])
    b = sig(w[3]*x0 + w[4]*x1 + w[5])
    p = sig(w[6]*a + w[7]*b + w[8])

    print(
        "Input:", (x0,x1),
        "Actual:", y,
        "Probability:", round(p,4),
        "Prediction:", round(p)
    )