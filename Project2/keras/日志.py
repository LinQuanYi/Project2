# coding:utf-8
import sys
import re
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "SimHei"  # 添加中文字体名称
plt.rcParams["axes.unicode_minus"] = False  # 由于更改了字体导致显示不出负号，此设置用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

in_log_path = './实验一.txt'  # 输入日志文件的位置
out_fig_path = './实验一.jpg'  # 输出图片的位置
f = open(in_log_path, encoding='utf-8')
accuracy_test1 = []
accuracy_test2 = []
accuracy_test3 = []

EPOCH = 0
target_str = ['val_accuracy: ', 'Epoch ']
while True:
    line = f.readline()
    if len(line) < 1:
        break
    for i in range(len(target_str)):
        str = target_str[i]
        idx = line.find(str)
        if idx != -1:
            if (i == 0):
                num = float(line[idx + len(str):idx + len(str) + 5])
                accuracy_test1.append(num)
            elif (i == 1):
                num = float(line[idx + len(str):idx + len(str) + 1])
                EPOCH = num
            else:
                pass
f.close()

in_log_path2 = './实验二.txt'  # 输入日志文件的位置
out_fig_path2 = './实验二.jpg'  # 输出图片的位置
f2 = open(in_log_path2, encoding='utf-8')
while True:
    line = f2.readline()
    if len(line) < 1:
        break
    for i in range(len(target_str)):
        str = target_str[i]
        idx = line.find(str)
        if idx != -1:
            if (i == 0):
                num = float(line[idx + len(str):idx + len(str) + 5])
                accuracy_test2.append(num)
            elif (i == 1):
                num = float(line[idx + len(str):idx + len(str) + 1])
                EPOCH = num
            else:
                pass
f2.close()

in_log_path3 = './实验三.txt'  # 输入日志文件的位置
out_fig_path3 = './实验一.jpg'  # 输出图片的位置
f3 = open(in_log_path3, encoding='utf-8')
while True:
    line = f3.readline()
    if len(line) < 1:
        break
    for i in range(len(target_str)):
        str = target_str[i]
        idx = line.find(str)
        if idx != -1:
            if (i == 0):
                num = float(line[idx + len(str):idx + len(str) + 5])
                accuracy_test3.append(num)
            elif (i == 1):
                num = float(line[idx + len(str):idx + len(str) + 1])
                EPOCH = num
            else:
                pass
f3.close()

_, ax1 = plt.subplots()
ax2 = ax1.twinx()
# 绘制实验一曲线图像，颜色为绿色'g'

ax1.plot(EPOCH * np.arange(len(accuracy_test1)), accuracy_test1, color='g', label='Dense(84)', linestyle='-')

# 绘制实验二曲线图像，颜色为黄色'y'
ax1.plot(EPOCH * np.arange(len(accuracy_test2)), accuracy_test2, color='y', label='Dense(256)', linestyle='-')
#
# 绘制实验三曲线图像，颜色为红色'r'
ax1.plot(EPOCH * np.arange(len(accuracy_test3)), accuracy_test3, color='r', label='Dense(512)', linestyle='-')


ax1.legend(loc=(0.7, 0.8))  # 使用二元组(0.7,0.8)定义标签位置
# ax2.legend(loc=(0.7, 0.72))
ax1.set_xlabel('EPOCH')  # 设置X轴标签
ax1.set_ylabel('Val_Accuracy')  # 设置Y1轴标签
# ax2.set_ylabel('accuracy')  # 设置Y2轴标签
plt.savefig(out_fig_path, dpi=100)  # 将图像保存到out_fig_path路径中，分辨率为100
plt.show()  # 显示图片
