import akshare as ak
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False

stock_df = ak.get_zdzk_fund_index(30, plot=False)  # 股票策略数据
futures_df = ak.get_zdzk_fund_index(32, plot=False)  # 管理期货策略数据

fig = plt.figure(111, figsize=(20, 10), dpi=300)
adjust_stock_df = stock_df["20150102":] / stock_df["20150102"] * 1000
adjust_stock_df.plot(linewidth=4)
adjust_futures_df = futures_df["20150102":] / futures_df["20150102"] * 1000
adjust_futures_df.plot(linewidth=4)
plt.title("智道智科股票策略和管理期货策略指数")
plt.legend()
plt.show()