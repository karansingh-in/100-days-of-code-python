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
    m,n = x.shape  # number of examples
    # n = x[0].shape  # number of features can't take it like this because we want a tuple of m,n
    dj_dw = np.zeros((n))
    dj_db = 0.0
    for i in range(m):
        error = (np.dot(w,x[i]) + b) - y[i]
        for j in range(n):
            dj_dw = error*x[i][j] + dj_dw
        dj_db = dj_db + error
    dj_db = dj_db/m
    dj_dw = dj_dw/m
    return dj_dw, dj_db

tempdj_dw, tempdj_db = compute_gradient(x_train,w_init,b_init,y_train)
print(tempdj_db)
print(tempdj_dw)

def gradient_descent(x, y, w_in, b_in, alpha, num_itr):
    
    for i in range(num_itr):
        dj_dw, dj_db = compute_gradient(x,w_in,b_in,y)
        w_in = w_in - (alpha*dj_dw)
        b_in = b_in - (alpha*dj_db)
    return w_in, b_in

w_test = np.zeros_like(w_init)
b_test = 0
alpha = 5.0e-7
iterations = 1000
w_final, b_final = gradient_descent(x_train,y_train,w_init,b_init,alpha,iterations)

m=x_train.shape[0]
for i in range(m):
    prediction = np.dot(w_final,x_train[i]) + b_final
    print(f'prediction : {prediction}, actual price : {y_train[i]}')