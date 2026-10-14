import pandas as pd
import sqlite3

read_data = pd.read_csv("Doctor_Data.csv")

connection_data = sqlite3.connect("triage_Data.db")

read_data.to_sql("Doctor",connection_data, if_exists = "replace", index = False)
connection_data.close()

