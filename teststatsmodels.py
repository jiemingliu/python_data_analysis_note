import numpy as np
import pandas as pd

def main():
	data = pd.DataFrame({
		'x0': [1, 2, 3, 4, 5],
		'x1': [0.01, -0.01, 0.25, -4.1, 0.],
		'y': [-1.5, 0., 3.6, 1.3, -2.],
		'prop':['aaa','bbb','ccc','d','ee']})
	model_cols = ['x0','x1']
	model = data.loc[:,model_cols]  # 选取列
	
	data = data.drop('prop',axis=1)  # 删除列
	data['category'] = pd.Categorical(['a', 'b', 'a', 'a', 'b'],
		categories=['a', 'b'])
	dummies = pd.get_dummies(data.category, prefix='category')
	data_with_dummies = data.drop('category', axis=1).join(dummies)
	print(data_with_dummies)
	
def main1():
	
	
if __name__ == "__main__":
	main();