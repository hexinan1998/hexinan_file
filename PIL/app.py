from PIL import Image


im = Image.open("cat.jpg","r")
print(im.size,im.format,im.mode)
# (121, 121) JPEG RGB
# size 是宽高像素  format 是图片格式  mode 表示图像的模式

im.save("dog.png",'png')

#上面的代码将图像重新保存成png格式。   
im.thumbnail((50,50),resample=Image.BICUBIC) # 第二个参数表示取样模式
im.show()

# 剪裁图像
box =  (20,20,60,60)  # 四个元素的元组  表示左上角 与 右下角 的坐标
region = im.crop(box)
region.show()

im_rotate_180 = im.transpose(Image.ROTATE_180)  # 可以找对应相翻转的角度
im_rotate_180.show()

#  要粘贴的对象 ，可以提供一个 左上角的 坐标
im.paste(region,(20,20),None)
im.show()

# 颜色分离
# r,g,b = im.split()
# r.show()
# g.show()
# b.show()

# 颜色合并
# im_merge = Image.merge("RGB",[b,r,g])
# im_merge.show()

# 改图像大小
#resize(size,resample,box)  # box 是指 要改变大小的区域
# im_resize = im.resize((200,200))

# convert(mode,matrix,dither,palette,colors)

# im_L = im.convert("L")
# im_L.show()
# im_rgb = im_L.convert("RGB")
# im_rgb.show()
# im_L.mode

'''
convert方法可以改变图像的mode,一般是在'RGB'(真彩图)、'L'(灰度图)、'CMYK'(压缩图)之间转换。
上面的代码就是首先将图像转化为灰度图，再从灰度图转化为真彩图。
值得注意的是,从灰度图转换为真彩图，虽然理论上确实转换成功了，但是实际上是很难恢复成原来的真彩模式的(不唯一)
'''
#过滤
# filter(filter)
#对像素点的操作
# point(lut,mode)
im_point = im.point(lambda x:x*1.5)
im_point.show()

#  还有图像增强    ， 与处理 gif 的类

# ImageEnhance    ImageSequence