第一部：numpy篇
import numpy as np
1.数组的初始化，
由列表初始化 data = np.array([11.11,22.2,3.3])
并且指定数组的类型 strings = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
随机生成 data = np.random.randn(2,3)
2.数组操作
转换数据类型 data1 = data.astype(np.int32)
数组可以用于任何算术运算，以及索引访问，切片操作
数组的索引可以用数组，但是两个数组的长度必须一致