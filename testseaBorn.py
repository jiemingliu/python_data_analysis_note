import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
	tips = pd.read_csv('examples/tips.csv');
	party_counts = pd.crosstab(tips['day'],tips['size']);
	party_counts = party_counts.loc[:,2:5];
	party_pcts = party_counts.div(party_counts.sum(1), axis=0)
	party_pcts.plot.bar();
	plt.show();
	
def main5():
	tips = pd.read_csv('examples/tips.csv');
	tips['tip_pct']=tips['tip']/(tips['total_bill']-tips['tip'])
	sns.barplot(x='tip_pct',y='day',data=tips,orient='h');
	plt.show()
	
def main6():
	tips = pd.read_csv('examples/tips.csv');
	tips['tip_pct']=tips['tip']/(tips['total_bill']-tips['tip'])
	#tips['tip_pct'].plot.hist(bins=50);  #直方图
	tips['tip_pct'].plot.density();  #密度图
	plt.show();
	
def main7():
	macro = pd.read_csv('examples/macrodata.csv')
	data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
	trans_data = np.log(data).diff().dropna()
	#sns.regplot('m1', 'unemp', data=trans_data)  #散布图
	sns.pairplot(trans_data,diag_kind='kde',plot_kws={'alpha':0.2})  #散布矩阵图
	plt.show();
	
if __name__ == "__main__":
	main7();