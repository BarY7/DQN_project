import numpy as np 
import pickle
import matplotlib.pyplot as plt

with open('./statistics.pkl', "rb") as pickled_file:
  pickled_data = pickle.load(pickled_file)
  print("OK")
  pickled_file.close()