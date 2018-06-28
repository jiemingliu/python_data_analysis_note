import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

def main():
	# points = np.arange(-5,5,0.01);
	# xs,ys = np.meshgrid(points,points);
	# z = np.sqrt(xs ** 2 + ys**2);
	
	x = np.linspace(-np.pi,np.pi,256,endpoint=True);
	C,S=np.cos(x),np.sin(x);
	plt.plot(x,C);
	plt.plot(x,S);
	plt.show();
	plt.savefig("test.png");
	
# figure 和 subplot
def main1():
	fig = plt.figure();
	ax1 = fig.add_subplot(2,2,1);
	ax2 = fig.add_subplot(2,2,2);
	ax3 = fig.add_subplot(2,2,3);
	ax4 = fig.add_subplot(2,2,4);
	plt.plot(np.random.randn(50).cumsum(),'k--');
	ax1.hist(np.random.randn(100),bins=20,color='r',alpha=0.1);
	ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30),color='y');
	fig.show();

# subplots
def main2():
	fig,axes = plt.subplots(2,3);
	plt.subplots_adjust(wspace=0,hspace=0);
	
	axes[0][0].plot(np.random.randn(30).cumsum(),'ko--');
	axes[0][1].plot(np.random.randn(30).cumsum(), color='r', linestyle='dashed', marker='o')
	fig.show();
	
# 标题、刻度等设置
def main3():
	fig = plt.figure();
	ax = fig.add_subplot(1,1,1);
	ax.plot(np.random.randn(1000).cumsum(),color='r');
	ticks = ax.set_xticks([0, 250, 500, 750, 1000]);
	labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],rotation=30, fontsize='small');
	ax.set_title('this is title');
	ax.set_xlabel('stage');
	fig.show();
	
# 图例
def main4():
	fig = plt.figure();
	ax = fig.add_subplot(1,1,1);
	ax.plot(randn(1000).cumsum(),'k',label='one',color='r');
	ax.plot(randn(1000).cumsum(),'k',label='two',color='b');
	ax.plot(randn(1000).cumsum(),'k',label='three',color="#ffff00");
	ax.legend(loc='best');
	fig.show();

if __name__ == "__main__":
	main4();