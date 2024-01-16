import pandas as pd
import numpy as numpy
import matplotlib.pyplot  as plt
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio
import seaborn as sns 
import os 


TRAIN_FILE_NAME = "UK_monthly_gdp.csv"
file_path = os.path.join(os.getcwd(),TRAIN_FILE_NAME)
print(os.getcwd())


data = pd.read_csv(TRAIN_FILE_NAME)
print(data.head(5))

data.drop(columns=['Recession'],inplace=True)
data['Time Period'] = pd.to_datetime(data['Time Period'], format='%Y-%m-%d')
data.set_index('Time Period', inplace=True)
quarterly_data = data.resample("Q").mean()
print(quarterly_data)

# estimating the recession by considering 2 consecutive quarters having GDP <0
quarterly_data['Recession']=((quarterly_data['GDP Growth'] < 0) & (quarterly_data['GDP Growth'].shift(1) < 0))
quarterly_data['Recession'].fillna(False,inplace=True)
print(quarterly_data.head(5))
print(quarterly_data.tail(5))

#saving the file
quarterly_data.to_csv("Recession_file_2022.csv")