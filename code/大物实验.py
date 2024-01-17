import numpy as np

from scipy.interpolate import CubicSpline

import matplotlib.pyplot as plt

# 设置中文字体为SimHei
plt.rcParams['font.sans-serif'] = ['SimHei']

# 提供的数据点（x和y）
x = [1.89, 1.99, 2.09, 2.19, 2.29, 2.39, 2.49, 2.59, 2.69]
y = [3.72, 5.44, 8.56, 14.6, 17.2, 10.3, 5.5, 3.2, 2.1]

# 使用样条插值
cs = CubicSpline(x, y)

# 生成平滑曲线的x值
x_smooth = np.linspace(min(x), max(x), 100)

# 计算平滑曲线的y值
y_smooth = cs(x_smooth)

# 绘制原始数据点和平滑曲线
plt.scatter(x, y, label='数据点')
plt.plot(x_smooth, y_smooth, label='拟合曲线', color='red')
plt.xlabel('工作频率/cm')
plt.ylabel('电压峰峰值幅度/V')
plt.legend()
plt.title('接收信号幅度与工作频率的关系')

# 显示图形
plt.show()
