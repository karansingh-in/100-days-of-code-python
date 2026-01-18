import numpy as np
x_train = np.array([[2104,5,1,45], [1416,3,2,40], [852,2,1,35]])
y_train = np.array([465, 232,178])

b_init = 785.1811367
w_init = np.array([0.39133, 18.7537, -53.360,-26.4213])

def predict(x,w,b):
    f = np.dot(w,x) + b
    return f

x_test = x_train[1]
f = predict(x_test, w_init, b_init)
print(f)

def compute_cost(x,w,b,y):
    j = 0.0
    m = x.shape[0]
    for i in range(m):
        f = predict(x[i],w,b)
        error = f - y[i]
        j = j + error**2
    j = j/(2*m)
    return j

# test = compute_cost(x_train, w_init,b_init, y_train)
# print(test)

def compute_gradient(x,w,b,y):
    m = x.shape[0]
    
    