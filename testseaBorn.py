import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pandas 内置的seaborn，可以简化美化绘图操作，并将DataFrame、Series数据同绘制结合起来。最终还是调用的matplotlib的api绘制
def main1():
	df = pd.DataFrame(np.random.randn(10, 4).cumsum(0),
		columns=['A', 'B', 'C', 'D'],
		index=np.arange(0, 100, 10));
	
	df.plot();
	plt.show();
	
def main2():
	fig, axes = plt.subplots(2, 1);
	data = pd.Series(np.random.rand(16), index=list('abcdefghijklmnop'));
	data.plot.bar(ax=axes[0], color='k', alpha=0.7);
	data.plot.barh(ax=axes[1], color='k', alpha=0.7);
	plt.show();
	
def main3():
	df = pd.DataFrame(np.random.rand(6,4),
		index=['one', 'two', 'three', 'four', 'five', 'six'],
		columns=pd.Index(['A', 'B', 'C', 'D'],name='Genus'));
	df.plot.bar();
	#df.plot.barh();
	plt.show();

def main4():
	tips = pd.read_csv('examples/tips.csx');
	party_counts = pd.crosstab(tips['day'],tips['size']);
	party_counts = party_counts.loc[:,2:5];
	party_pcts = party_counts.div(party_counts.sum(1), axis=0)
	party_pcts.plot.bar();
	plt.show();
	

if __name__ == "__main__":
	main4();