import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
	main();