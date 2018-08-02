from PIL import Image
import numpy as np

"""
    图片转换为手绘风格
"""

a = np.array(Image.open('D:/a/b.jpg').convert('L')).astype('float')  # 变灰度图
print(a)
depth = 10.                         # 深度值 0~100
grad = np.gradient(a)               # 取图像灰度的梯度值  是一个关于x，y的数据对
grad_x, grad_y = grad               # 付给x，y分别取横纵图像的灰度值
grad_x = grad_x * depth / 100.      # 添加深度对梯度的影响因素 并/100 进行归一化
grad_y = grad_y * depth / 100.


A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x / A
uni_y = grad_y / A
uni_z = 1. / A                        

vec_e1 = np.pi/2.2                  # 光源的俯视角度，弧度值
vec_az = np.pi/4.                   # 光源的方位角度，弧度值
dx = np.cos(vec_e1) * np.cos(vec_az)    # 光源对x轴的影响
dy = np.cos(vec_e1) * np.sin(vec_az)
dz = np.sin(vec_e1)

b = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)    # 光源归一化
b = b.clip(0, 255)

im = Image.fromarray(b.astype('uint8'))
im.save('D:/a/b1.jpg')
print("转换完成！")
