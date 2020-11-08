import cvxpy as cp
from scripts.model import lambModel
import matplotlib.pyplot as plt
import numpy as np



if __name__ == "__main__":

    """
     建立模型
    """
    numberOfSidewalk = 10
    numberOfLambs = 5
    model = lambModel(numberOfSidewalk,numberOfLambs)

    """
    方法1
        最小二乘
    """
    A = model.A_
    Ik = model.Iks /255
    # pp = np.linalg.inv(A.transpose()@A)@A.transpose()@Ik
    p1 = cp.Variable(numberOfLambs)
    objective = cp.Minimize(cp.sum_squares(A @ p1 - Ik))
    constraints = [0 <= p1, p1 <= 2]
    prob = cp.Problem(objective, constraints)
    var_s1= prob.solve()

    """
    方法2
        线性规划
    """
    A = model.A_
    Ik = model.Iks / 255
    # pp = np.linalg.inv(A.transpose()@A)@A.transpose()@Ik
    p2 = cp.Variable(numberOfLambs)
    objective = cp.Minimize(cp.norm(A @ p2 - Ik))
    constraints = [0 <= p2, p2 <= 2]
    prob = cp.Problem(objective, constraints)
    var_s2 = prob.solve()


    """
        方法3
           Chebyshev APPROXIMATION
        """
    A = model.A_
    Ik = model.Iks / 255
    # pp = np.linalg.inv(A.transpose()@A)@A.transpose()@Ik
    p3 = cp.Variable(numberOfLambs)
    objective = cp.Minimize(cp.max(A @ p3 - Ik))
    constraints = [0 <= p3, p3 <= 2]
    prob = cp.Problem(objective, constraints)
    var_s3 = prob.solve()


    """
    可视化
    """

    ax = plt.subplot(1,3,1)
    ans = model.getAnsMap(p1.value)
    plt.imshow(ans)
    ax.set_title("lost=" + np.str(var_s1))

    ax = plt.subplot(1, 3, 2)
    ans = model.getAnsMap(p2.value)
    ax.set_title("lost=" + np.str(var_s2))
    print(ans)
    plt.imshow(ans)

    ax = plt.subplot(1, 3, 3)
    ans = model.getAnsMap(p3.value)
    print("max",np.max(ans),np.min(ans))
    print(ans)
    plt.imshow(ans)
    ax.set_title("lost="+ np.str(var_s3))
    plt.show()
