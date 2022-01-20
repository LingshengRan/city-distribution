from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def Pic(data):
    x = []
    for i in range(len(data)):
        x.append(data[i][0])
    y = []
    for i in range(len(data)):
        y.append(data[i][1])
    return x, y

def sample(data, sd):
    # plt.figure()
    for i in range(len(data)):
        x, y = Pic(data[i])
        x.append(x[0])  # 增加第一个坐标使得矩形封闭
        y.append(y[0])

        plt.plot(x, y, c='r',linewidth=1)

    x.append(x[1])

    y.append(y[1])


    # 求两条邻边的向量
    new_data = []
    Qi_x_list = []
    Qi_y_list = []
    for i in range(len(x)):
        if i < (len(x) - 2):
            # print("=========")
            # print(x[i],y[i])
            # print(x[i+1], y[i+1])
            # 求边的长度
            d1 = ((x[i + 1] - x[i]) ** 2 + (y[i + 1] - y[i]) ** 2) ** 0.5
            d2 = ((x[i + 1] - x[i + 2]) ** 2 + (y[i + 1] - y[i + 2]) ** 2) ** 0.5
            # 两条边的夹角
            # 内积ab,sinA
            # ab=(x[i+1]-x[i])*(y[i+1]-y[i])+(x[i+1]-x[i+2])*(y[i+1]-y[i+2])
            ab = (x[i + 1] - x[i]) * (x[i + 1] - x[i + 2]) + (y[i + 1] - y[i]) * (y[i + 1] - y[i + 2])
            cosA = ab / (d1 * d2)

            if cosA > 0:

                sinA = (1 - cosA ** 2) ** 0.5

                # 向量V1,V2的坐标
                dv1 = sd / sinA  # V1,V2长度相等
                v1_x = (dv1 / d1) * (x[i + 1] - x[i])
                v1_y = (dv1 / d1) * (y[i + 1] - y[i])
                v2_x = (dv1 / d2) * (x[i + 1] - x[i + 2])
                v2_y = (dv1 / d2) * (y[i + 1] - y[i + 2])
                PiQi_x = v1_x + v2_x
                PiQi_y = v1_y + v2_y
                Qi_x = PiQi_x + x[i + 1]
                Qi_x_list.append(Qi_x)
                Qi_y = PiQi_y + y[i + 1]
                Qi_y_list.append(Qi_y)
                # new_data.append(zip(Qi_x, Qi_y))
            elif cosA <= 0:
                # x[]
                # 判断凹凸点（叉积）
                P1P3_x = x[i + 2] - x[i]
                P1P3_y = y[i + 2] - y[i]
                P1P2_x = x[i + 1] - x[i]
                P1P2_y = y[i + 1] - y[i]
                # P=P1P3 x P1P2
                P = (P1P3_y * P1P2_x) - (P1P3_x * P1P2_y)
                # 为凹时
                if P > 0:
                    sinA = -((1 - cosA ** 2) ** 0.5)

                    # 向量V1,V2的坐标
                    dv1 = sd / sinA  # V1,V2长度相等
                    v1_x = (dv1 / d1) * (x[i + 1] - x[i])
                    v1_y = (dv1 / d1) * (y[i + 1] - y[i])
                    v2_x = (dv1 / d2) * (x[i + 1] - x[i + 2])
                    v2_y = (dv1 / d2) * (y[i + 1] - y[i + 2])
                    PiQi_x = v1_x + v2_x
                    PiQi_y = v1_y + v2_y
                    Qi_x = PiQi_x + x[i + 1]
                    Qi_x_list.append(Qi_x)
                    Qi_y = PiQi_y + y[i + 1]
                    Qi_y_list.append(Qi_y)
                elif P < 0:
                    sinA = -((1 - cosA ** 2) ** 0.5)

                    # 向量V1,V2的坐标
                    dv1 = -sd / sinA  # V1,V2长度相等
                    v1_x = (dv1 / d1) * (x[i + 1] - x[i])
                    v1_y = (dv1 / d1) * (y[i + 1] - y[i])
                    v2_x = (dv1 / d2) * (x[i + 1] - x[i + 2])
                    v2_y = (dv1 / d2) * (y[i + 1] - y[i + 2])
                    PiQi_x = v1_x + v2_x
                    PiQi_y = v1_y + v2_y
                    Qi_x = PiQi_x + x[i + 1]
                    Qi_x_list.append(Qi_x)
                    Qi_y = PiQi_y + y[i + 1]
                    Qi_y_list.append(Qi_y)
            # elif cosA == 0:
            #     sinA = 1
            #     # print('sinA')
            #     # print(sinA)
            #     # 向量V1,V2的坐标
            #     dv1 = sd / sinA  # V1,V2长度相等
            #     v1_x = (dv1 / d1) * (x[i + 1] - x[i])
            #     v1_y = (dv1 / d1) * (y[i + 1] - y[i])
            #     v2_x = (dv1 / d2) * (x[i + 1] - x[i + 2])
            #     v2_y = (dv1 / d2) * (y[i + 1] - y[i + 2])
            #     PiQi_x = v1_x + v2_x
            #     PiQi_y = v1_y + v2_y
            #     Qi_x = PiQi_x + x[i + 1]
            #     Qi_x_list.append(Qi_x)
            #     Qi_y = PiQi_y + y[i + 1]
            #     Qi_y_list.append(Qi_y)
            #     # new_data.append(zip(Qi_x, Qi_y))
    Qi_x_list.append(Qi_x_list[0])
    Qi_y_list.append(Qi_y_list[0])
    # print(Qi_x_list)
    # print(Qi_y_list)
    plt.plot(Qi_x_list, Qi_y_list, c='b', linewidth=1)
    # plt.show()

    return Qi_x_list,Qi_y_list


if __name__ == '__main__':
    data=[[(526.5,586.0),(567.5,586.0),(567.5,633.5),(526.5,633.5)]]
    data2=[[(640, 860), (840, 860), (840, 560), (640, 560)]]
    # data = [[(10, 10), (10, 20), (15, 20), (15, 17), (30, 15), (25, 0), (20, 12)]]
    outer_boundary = 4  # 安全距离
    sample(data, outer_boundary)
    sample(data2, outer_boundary)

# (553,607):[[(526.5,586.0),(567.5,586.0),(567.5,633.5),(526.5,633.5)]],
#
