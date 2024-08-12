import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None



def predict_price(location,sqft,bath,bhk):
  try:
    loc_index = __data_columns.index(location.lower())
  except:
    loc_index = -1

  x = np.zeros(len(__data_columns))
  x[0]=sqft
  x[1]=bath
  x[2]=bhk
  if loc_index>=0:
    x[loc_index]=1

  return round(__model.predict([x])[0],2)

def get_location_names():
  return __locations

def loadArtifacts():
  print('loading artifacts...')
  global __locations
  global __data_columns
  global __model

  with open("./artifacts/columns.json",'r') as f:
    __data_columns = json.load(f)['data_columns']
    __locations = __data_columns[3:]

  with open('./artifacts/Bangaluru_House_Data.pickle','rb') as f:
    __model = pickle.load(f)
  print('loading Artifacts finished')


if __name__ == "__main__":
  loadArtifacts()
  get_location_names()
 
    
  