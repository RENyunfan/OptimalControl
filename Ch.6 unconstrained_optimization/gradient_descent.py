import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2
def dot_f(x):
    return 2*x



def exactLineSearch(epsilon, x0, LR):
    """
        精确直线搜索
    """
    xs = [x0]
    ys = [f(x0)]
    x= x0
    it_times = 0
    while (abs(dot_f(x)) > epsilon):
        it_times += 1
        x = x - dot_f(x) * LR
        xs.append(x)
        ys.append(f(x))
        print(it_times)

    t = np.linspace(-2, 2, 100)
    y = f(t)
    y_dot = dot_f(t)
    fig = plt.figure()
    plt.plot(t, y)
    plt.plot(xs, ys)
    plt.show()

def backtracingLineSearch(epsilon, x0, LR):
    """
    回溯直线搜索
    :return:
    """
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
    exactLineSearch(1e-4, -2, 0.7)

