import numpy as np 
import pickle
import matplotlib.pyplot as plt
import pandas as pd

with open('./statistics copy.pkl', "rb") as pickled_file:
  pickled_data = pickle.load(pickled_file)
  print("OK")
  statistics_df = pd.DataFrame(pickled_data)
  statistics_df.plot(xlabel = 't',ylabel = 'reward', title = 'Reward vs. Time').get_figure().savefig('./4M' + '.png') 
  pickled_file.close()