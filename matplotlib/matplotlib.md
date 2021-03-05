# Matplotlib

------

## 1  base

```python
import matplotlib.pyplot as plt
# 布置画板
fig = plt.figure()
```

```python
fig = plt.figure()
# 在画板的  1行 1列 第一个位置 给出图表
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title="An Example Axes",
       ylabel="YYYY", xlabel="XXXX")
plt.show()
```

![](D:\download_git\hexinan_study\matplotlib\img\01.png) 

```python
fig = plt.figure()
ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(224)
```

 ![](D:\download_git\hexinan_study\matplotlib\img\02.png)

```python
fig , axes = plt.subplots(nrows=2, ncols=2)
axes[0,0].set(title='Upper Left')
axes[0,1].set(title='Upper Right')
axes[1,0].set(title='Lower Left')
axes[1,1].set(title='Lower Right')
```

```python
#  绘制简单的 折线图
plt.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
plt.xlim(0.5, 4.5)
plt.show()
```

## 2. 基本绘图 2 D

##  

```python
#################### 绘制 线

x = np.linspace(0, np.pi)
y_sin = np.sin(x)
y_cos = np.cos(x)

fig,ax = plt.subplots(nrows=2, ncols=2)
[[ax1, ax2],[ax3, ax4]] = ax

ax1.plot(x, y_sin)
ax2.plot(x, y_sin, 'go--', linewidth=2, markersize=12)
ax3.plot(x, y_cos, color='red', marker='+', linestyle='dashed')
```

![](D:\download_git\hexinan_study\matplotlib\img\03.png) 

```python
x = np.linspace(0, 10, 200)
data_obj = {'x': x,
            'y1': 2 * x + 1,
            'y2': 3 * x + 1.2,
            'mean': 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1}

fig, ax = plt.subplots()

#填充两条线之间的颜色
ax.fill_between('x', 'y1', 'y2', color='yellow', data=data_obj)

# Plot the "centerline" with `plot`
ax.plot('x', 'mean', color='black', data=data_obj)

plt.show()
```

![](D:\download_git\hexinan_study\matplotlib\img\04.png) 

```python
########   散点图
x = np.arange(10)
y = np.random.randn(10)
plt.scatter(x, y, color='red', marker='+')
plt.show()
```

```python
np.random.seed(1)
x = np.arange(5)
y = np.random.randn(5)

fig, axes = plt.subplots(ncols=2, figsize=plt.figaspect(1./2))

vert_bars = axes[0].bar(x, y, color='lightblue', align='center')
horiz_bars = axes[1].barh(x, y, color='lightblue', align='center')
#在水平或者垂直方向上画线
axes[0].axhline(0, color='gray', linewidth=2)
axes[1].axvline(0, color='gray', linewidth=2)
plt.show()
```

```python
# 显示图片

plt.figure("Image") # 图像窗口名称
# 此处的 img 可以是 numpy , list , PIL img ,tensor
plt.imshow(img)
plt.axis('on') # 关掉坐标轴为 off
plt.title('image') # 图像题目
plt.show()
```

