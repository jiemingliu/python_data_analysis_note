import pandas as pd
import numpy as np
from pandas import Series,DataFrame

# 在时间序列的处理上，pandas有很多细节，比如时区的处理，比如偏移量的处理，频率等

# 使用时间序列在Series数据结构上，DataFrame同理
from datetime import datetime
def main1():
	dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
			datetime(2011, 1, 7), datetime(2011, 1, 8),
			datetime(2011, 1, 10), datetime(2011, 1, 12)]
	
	ts = pd.Series(np.random.randn(6), index=dates)
	print(ts);print("----------------")
	print(ts.index)

def main2():
	longer_ts = pd.Series(np.random.randn(1000),
		index=pd.date_range('1/1/2000', periods=1000))
	print(longer_ts);print("---------")
	print(longer_ts['2002'])
	print(longer_ts[datetime(2002,1,1)]);  #可以按年或年月或年月日进行切片
	
# 区间定义
def main3():
	index = pd.date_range('2012-04-01', '2012-06-01')
	print(index)
	
if __name__ == "__main__":
	main3();