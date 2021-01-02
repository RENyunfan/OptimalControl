import numpy as np
import matplotlib.pyplot as plt

# def f(x):
#     return x**2
# def dot_f(x):
#     return 2*x

def f(x):
    return x[0]**2+x[1]**2

def dot_f(x):
    dx = np.array([2*x[0], 2*x[1]])
    return dx

def exactLineSearch(epsilon, x0, LR):

    xs = [x0]
    x= xs[0]
    it_times = 0
    while (np.linalg.norm(dot_f(x)) > epsilon):
        it_times += 1
        x = x - dot_f(x) * LR
        xs.append(x)
        print(it_times)

    fig = plt.figure()
    plt.plot(xs[0], xs[1])
    plt.show()

def backtracingLineSearch(epsilon, x0, LR):

    xs = [x0]
    ys = [f(x0)]
    it_times=0;
    alpha = 0.3
    beta = 0.5
    LR = 1
    x = x0
    while(abs(f(x)) > epsilon):
        it_times+=1
        dx = -dot_f(x) * LR * alpha
        if(f(x + LR * dx) > f(x) + alpha * LR * dot_f(x)*(dx)):
            LR = LR * beta
        x = x + LR * dx
        xs .append(x)
        ys.append(f(x))
        print(x)
    t = np.linspace(-2, 2, 100)
    y = f(t)
    y_dot = dot_f(t)
    fig = plt.figure()
    plt.plot(t, y)
    plt.plot(xs, ys)
    plt.scatter(xs,ys,color="coral")
    plt.show()

if __name__ == "__main__":
    # backtracingLineSearch(1e-4,-2,1)
    # x0 = np.array([-2,-2])
    # exactLineSearch(1e-4, x0, 0.7)
    xs = np.random.rand(10)
    ys = np.random.rand(10)
    plt.plot(xs,ys)
    plt.show()


