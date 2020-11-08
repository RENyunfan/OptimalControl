import matplotlib.pyplot as plt
import numpy as np

class lambModel:

    """
    构造函数
        n 段路和 m 盏灯
    """
    n_ = 0
    m_ = 0
    mapSize_ = np.zeros(2)
    pix2meter = 240
    lambs_ = []
    mapPos_ = []
    ans_ = []
    map_ = []
    p_ = []
    Iks = []
    A_ = []
    def __init__(self, n, m, mapSize=[480, 640]):
        self.n_ = n
        self.m_ = m
        self.mapSize_ = mapSize
        map = np.zeros((480, 640))
        cnt = np.linspace(50, 255, n)
        # cnt = np.random.rand(n) * 255
        self.Iks = cnt
        self.lambs_ = self.getLambPose() / self.pix2meter
        self.mapPos_ = self.getMapPose() / self.pix2meter
        for i in range(440, 460):
            for j in range(0, 640):
                map[i][j] = int(cnt[int(j / (640 / n))])
        self.map_ = map
        self.calcA()

    """
    生成直线地图坐标
        参数：路段数目n
             地图大小MapSize
        输出：n*2的numpy数组，第一列表示路段中点位置，第二列表示路段法线方向，默认为0
    """
    def getMapPose(self):
        mapPos = []
        for i in range(0, self.n_):
            mapPos.append([self.mapSize_[1] // self.n_ * i + self.mapSize_[1] // self.n_ // 2, 0])
        mapPos = np.array(mapPos)
        return mapPos

    """
    随机生成灯坐标
        输入n灯的个数
        地图尺寸
    """

    def getLambPose(self):
        lambPos_y = np.random.rand(self.m_) * 30
        lambPos_y = lambPos_y + self.mapSize_[0] // 2
        # print(lambPos_y)
        lambPos_x = np.random.rand(self.m_)
        # print(lambPos_x)
        lambPos_x = lambPos_x * self.mapSize_[1]
        lamp = [lambPos_x, lambPos_y]
        lamp = np.array(lamp).transpose()
        # print(lamp)
        return lamp

    """
    计算系数矩阵A
    """
    def calcA(self):
        for i in range(0, self.mapPos_.shape[0]):
            """
            计算第k个路点
            """
            now_r = []
            for j in range(0, self.lambs_.shape[0]):
                r = np.sqrt((self.mapPos_[i, 0] - self.lambs_[j, 0]) ** 2 + ((self.lambs_[j, 1])) ** 2)
                now_ = 1 / r ** 2
                now_ = now_ * max(self.lambs_[j, 1] / r, 0)
                now_r.append(now_)
            self.A_.append(now_r)
        self.A_ = np.array(self.A_)
        # return self.A_
    def rangeCut(self,data):
        if(data>255):
            data = 255
        return max(0,data)
    def drawAns(self):

        amap = self.map_.copy()
        n = 10
        # print(amap)
        Iks = (self.ans_ / max(self.ans_) * 255)
        step = 640 // Iks.shape[0]
        for k in range(0, n):
            amap[460:480, int(640 // n * k):int(640 // n * (k + 1))] =self.rangeCut( int(Iks[k]))

        return amap

    def drawBox(self, boxSize=10):
        cnt = 0
        amap = self.map_
        for pos in self.lambs_:
            amap[int((pos[1]) * self.pix2meter - boxSize):int((pos[1]) * self.pix2meter + boxSize),
            int((pos[0]) * self.pix2meter - boxSize):int((pos[0]) * self.pix2meter + boxSize)] \
                = self.rangeCut(int(self.p_[cnt] / max(self.p_) * 255))
            # print(int(self.p_[cnt] / max(self.p_) * 255))
            cnt = cnt + 1


        return amap

    def showAnswer(self, p):
        self.p_ = p
        map_box = self.drawBox()
        self.ans_ = self.A_ @ p
        map_ans = self.drawAns()
        map_ans[0:440, :] = map_box[0:440, :]
        plt.imshow(map_ans)
        plt.show()

    def getAnsMap(self, p):
        self.p_ = p
        map_box = self.drawBox()
        self.ans_ = self.A_ @ p
        self.ans_ = self.ans_ / max(self.ans_) * 255
        map_ans = self.drawAns()
        map_ans[0:440, :] = map_box[0:440, :]
        return map_ans