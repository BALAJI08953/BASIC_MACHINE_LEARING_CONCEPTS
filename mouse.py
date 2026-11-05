import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
mouse={
    "size":[1.4,2.6,1.0,3.7,5.5,3.2,3.0,4.9,6.3],
    "weight":[0.9,1.8,2.4,3.5,3.9,4.4,5.1,5.6,6.3],
    "tail":[0.7,1.3,0.7,2.0,3.6,3.0,2.9,3.9,4.0]
}
my_mouse=pd.DataFrame(mouse)
print(my_mouse)
my_draw=plt.scatter(my_mouse['weight'],my_mouse['size'])
print(my_draw)
plt.show()