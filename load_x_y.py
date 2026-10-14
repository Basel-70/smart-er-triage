import pandas as pd
import sqlite3

#---------------------------------------------{prepare the data}---------------------------------------------------------------------------------------------

def load_Training_data():

 connection = sqlite3.connect("triage_Data.db")
 
 get_data = pd.read_sql_query("SELECT * FROM patients",connection)
 
 
 get_data["sex"] = get_data["sex"].map({"M": 1, "F": 0})
 

 x_feature = get_data[["age","sex","systolic_bp","diastolic_bp", "heart_rate" ,"respiratory_rate" ,"temperature","spo2", "pain_score","chief_complaint"]]
 y_target = get_data["esi_level"]

 x_feature = pd.get_dummies(
   x_feature,
   columns = ["chief_complaint"],
   dtype = int
  )
 
 return x_feature , y_target , get_data

def load_Doctor_data():

 connection = sqlite3.connect("triage_Data.db")
 get_data = pd.read_sql_query("SELECT * FROM Doctor", connection)
 
 return get_data 