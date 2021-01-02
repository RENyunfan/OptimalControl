import numpy as np
import matplotlib.pyplot as plt

# def f(x):
#     return x**2
# def dot_f(x):
#     return 2*x

def f(x):
    return (x[0]-0.5)**2+(x[1])**2*2 +(x[0]+0.5)**2+(x[1])**2*2

def fs(x,y):
    return (x-3)**2+y**2*2 + (x+3)**2+y**2*1



def dot_f(x):
    dx = np.array([4*x[0], 4*2*x[1]])
    return dx
def ddot_f(x):
    dx = np.array([[4,0],[0,8]])
    return dx

def exactLineSearch(ax,epsilon, x0, LR):

    xs = [x0]
    x= x0
    it_times = 0
    while (np.linalg.norm(dot_f(x)) > epsilon):
        it_times += 1
        x = x - dot_f(x) * LR
        xs.append(x)

    xs = np.array(xs)
    n = 1000
    x = np.linspace(-2, 2, n)
    y = np.linspace(-2, 2, n)
    X, Y = np.meshgrid(x, y)
    ax.contourf(X, Y, fs(X, Y))
    ax.plot(xs[:,0], xs[:,1],color="white")
    ax.scatter(xs[:, 0], xs[:, 1],color="coral")
    ax.set_title("GD")
    tt = "it_time: " + str(it_times)
    ax.text(-1.8, 1.6, tt)


def backtracingLineSearch(ax,epsilon, x0, LR):
    xs = [x0]
    x = x0
    it_times=0;
    alpha = 0.3
    beta = 0.5
    while (np.linalg.norm(dot_f(x)) > epsilon):
        it_times+=1
        dx = -dot_f(x) * LR * alpha
        # print (dot_f(x).transpose().dot(dx))
        if(f(x + LR * dx) > f(x) + alpha * LR * dot_f(x).dot(dx)):
            LR = LR * beta
        x = x + LR * dx
        xs .append(x)
    xs = np.array(xs)

    n = 1000
    x = np.linspace(-2, 2, n)
    y = np.linspace(-2, 2, n)
    X, Y = np.meshgrid(x, y)
    ax.contourf(X, Y, fs(X, Y))
    ax.plot(xs[:, 0], xs[:, 1], color="white")
    ax.scatter(xs[:, 0], xs[:, 1], color="coral")
    ax.set_title("Auto GD")
    tt = "it_time: " + str(it_times)
    ax.text(-1.8, 1.6, tt)


def newtown(ax,epsilon, x0, LR):
    xs = [x0]
    x = x0
    it_times = 0

    while (np.linalg.norm(dot_f(x)) > epsilon):
        it_times += 1
        x = x - dot_f(x).dot( LR * np.linalg.inv(ddot_f(x)))
        xs.append(x)
    xs = np.array(xs)
    n = 1000
    x = np.linspace(-2, 2, n)
    y = np.linspace(-2, 2, n)
    X, Y = np.meshgrid(x, y)
    ax.contourf(X, Y, fs(X, Y))
    ax.plot(xs[:, 0], xs[:, 1], color="white")
    ax.scatter(xs[:, 0], xs[:, 1], color="coral")
    ax.set_title("Newton")
    tt = "it_time: " + str(it_times)
    ax.text(-1.8, 1.6, tt)


def fg(ax,epsilon, x0, LR):
    xs = [x0]
    x = x0
    it_times = 0
    p = -dot_f(x0)
    xp = x0
    while (np.linalg.norm(dot_f(x)) > epsilon):
        it_times += 1
        xp = x
        x = x + LR * p
        alpha = np.linalg.norm(x) / np.linalg.norm(xp)
        p = -dot_f(x) + alpha**2 * p
        x = x - dot_f(x).dot( LR * np.linalg.inv(ddot_f(x)))
        xs.append(x)
    xs = np.array(xs)
    n = 1000
    x = np.linspace(-2, 2, n)
    y = np.linspace(-2, 2, n)
    X, Y = np.meshgrid(x, y)
    ax.contourf(X, Y, fs(X, Y))
    ax.plot(xs[:, 0], xs[:, 1], color="white")
    ax.scatter(xs[:, 0], xs[:, 1], color="coral")
    ax.set_title("FG")
    tt = "it_time: "+str(it_times)
    ax.text(-1.8, 1.6, tt)



if __name__ == "__main__":
    x0 = np.array([-2,-2])
    fig = plt.figure()
    ax1 = plt.subplot(2,2,1)
    backtracingLineSearch(ax1,1e-4,x0,1)
    ax2 = plt.subplot(2,2,2)
    exactLineSearch(ax2,1e-4, x0, 0.2)
    ax3 = plt.subplot(2, 2, 3)
    newtown(ax3, 1e-4, x0, 0.9)
    ax4 = plt.subplot(2, 2, 4)
    fg(ax4, 1e-4, x0, 0.15)
    plt.show()


