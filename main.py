#%%
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf


#%%
class Plot:
    def plotcloseCsv(csv, sampleSize):
        df = pd.read_csv(Path().joinpath('data', csv))
        sample_df = df.sample(sampleSize)
        plt.plot(sample_df['Date'], sample_df['Close'])
        plt.show()

    def plotcloseYf(ticker, start, end):
        df = yf.download(ticker,start,period=end)["Adj Close"]
        plt.plot(df)
        plt.show()


#%%
class SignificantDates:
    apple = {
        # Announcement not released
        'Vision Pro Glasses': '2023-06-05',
        # Announcement not released
        'Iphone 15 Pro': '2023-09-12',
        # Results
        'Third Quarter Results': '2023-08-03'
    }

    samsung = {
        # Released
        'Z fold 5': '2023-08-11',
        # Released
        'Galaxy Watch 5': '2022-08-26',
        # Released
        'Galaxy Tab S9': '2023-08-11'
    }


#%%
Plot.plotcloseCsv('GOOG.csv',10)

#%%
Plot.plotcloseYf("AAPL","2023-06-01","2023-06-10")

#%%
Plot.plotcloseYf("BC94.L",SignificantDates.samsung['Z fold 5'],"1week")

#%%
Plot.plotcloseYf("AAPL",SignificantDates.apple['Vision Pro Glasses'], "1week")