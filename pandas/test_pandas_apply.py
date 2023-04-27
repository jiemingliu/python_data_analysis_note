import numpy as np
import pandas as pd

def main():
	fruits = ['orange', 'orange', 'apple', 'apple'] * 2
	N = len(fruits)
	df = pd.DataFrame({'fruit': fruits,
		'basket_id': np.arange(N),
		'count': np.random.randint(3, 15, size=N),
		'weight': np.random.uniform(0, 4, size=N)},columns=['basket_id', 'fruit', 'count', 'weight'])
	print(df);print("-------------------")
	df['fruit'] = df['fruit'].astype('category')  # 转化列数据类型为分类
	
def main1():
	N = 10000000
	draws = pd.Series(np.random.randn(N))
	labels = pd.Series(['foo', 'bar', 'baz', 'qux']*(N//4))
	cates = labels.astype('category')
	print(labels.memory_usage())
	print(cates.memory_usage())

if __name__ == "__main__":
	main1();