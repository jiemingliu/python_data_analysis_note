import pandas as pd
import numpy as np
from pandas import Series,DataFrame  #两种数据结构，类似于键值对和C#的DataTable

def main1():
	points = pd.Series([5,9,-3,14,44,32]);
	print(points);
	print(pd.isnull(points));
	
	data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
			'year': [2000, 2001, 2002, 2001, 2002, 2003],
			'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]};
	frame = pd.DataFrame(data);
	print(frame);
	print(frame.year);

# 测试pandas的分组能力
def main2():
	df = pd.DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],
		'key2' : ['one', 'two', 'one', 'two', 'one'],
		'data1' : np.random.randn(5),
		'data2' : np.random.randn(5)})
	grouped = df['data1'].groupby(df['key1'])
	print(grouped.mean())
	print(df.groupby('key1').mean())
	print(df.groupby(['key1','key2']).mean())
	
	for name,group in df.groupby('key1'):  #迭代 GroupBy 对象
		print(name)
		print(group)
		
# 使用时间序列在Series数据结构上，DataFrame同理
from datetime import datetime
def main3():
	dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
			datetime(2011, 1, 7), datetime(2011, 1, 8),
			datetime(2011, 1, 10), datetime(2011, 1, 12)]
	
	ts = pd.Series(np.random.randn(6), index=dates)
	print(ts);print("----------------")
	print(ts.index)

def main33():
	longer_ts = pd.Series(np.random.randn(1000),
		index=pd.date_range('1/1/2000', periods=1000))
	print(longer_ts);print("---------")
	print(longer_ts['2002'])
	print(longer_ts[datetime(2002,1,1)]);  #可以按年或年月或年月日进行切片
	
	
if __name__ == '__main__':
	main33();