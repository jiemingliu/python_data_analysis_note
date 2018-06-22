采用redis作为缓存数据库
前篇：redis篇
启动redis服务，cmd窗口，使用cd命令切换目录到 C:\redis 运行 redis-server.exe redis.windows.conf
在配置文件redis.windows.conf中，可以修改host，端口等参数

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
3.数组矢量化操作，矩阵计算

第二部：pandas篇
1.pandas可以处理文本类型，分隔符格式文件，json，xml，html，二进制，HDF5,Microsoft Excel，数据库等类型的数据
2.数据整合：数据缺失，数据转换，聚合、合并、重塑数据
import pandas as pd