import yfinance as yf
import matplotlib.pyplot as plt

btc = yf.download('BTC-USD', start='2023-01-01')

plt.figure(figsize=(10,5))
plt.plot(btc.index, btc['Close'])
plt.title('Bitcoin Price Trend')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid()

plt.show()
