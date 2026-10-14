import pandas as pd
from load_x_y import load_Training_data
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter


def new_patient():

 x_feature, y_target, get_data = load_Training_data()

 complaints = [
  "Moderate abdominal pain",
  "Laceration requiring sutures",
  "Back pain",
  "Vomiting",
  "Headache severe",
  "Fever",
  "Minor injury",
  "Cough",
  "Cold symptoms",
  "Sprain",
  "Rash",
  "Mild abdominal discomfort",
  "Stroke symptoms",
  "Severe abdominal pain",
  "High fever with confusion",
  "Severe shortness of breath",
  "Chest pain",
  "Head injury with LOC",
  "Medication question",
  "Follow-up visit",
  "Minor rash",
  "Prescription refill",
  "Chronic pain stable",
  "Unresponsive",
  "Cardiac arrest",
  "Massive hemorrhage",
  "Seizure ongoing",
  "Severe respiratory distress"
 ]

 complaints_completer = WordCompleter(
  complaints,
  ignore_case=True,
  sentence=True
 )

 


 patient = {
  "age" : int(input("❇️  Enter the patient age : ")),
  "sex" : input("❇️  Enter the patient gender M or F: "),
  "systolic_bp" : float(input("❇️  Enter the systolic bp : ")), # ضغط الدم الانقباضي 
  "diastolic_bp" : float(input("❇️  Enter the diastolic bp : ")), #  ضغط الدم الانبساطي
  "heart_rate" : float(input("❇️  Enter the heart rate : ")),
  "respiratory_rate" : float(input("❇️  Enter the respiratory rate : ")),# معدل التنفس
  "temperature" : float(input("❇️  Enter the temperature : ")),
  "spo2" : float(input("❇️  Enter the Saturation of Peripheral Oxygen : ")), # نسبة تشبع الأكسجين في الدم
  "pain_score" : int(input("❇️  Enter the pain from (0 to 10) : ")),
  
 }

 complaint = prompt(
    "Enter the Chief Complaint : ",

   completer=complaints_completer)
  
 patient["chief_complaint"] = complaint
   
 new_patient_df = pd.DataFrame([patient])
 new_patient_df["sex"] = new_patient_df["sex"].map({"M": 1, "F": 0})

 new_patient_df = pd.get_dummies(
  new_patient_df,
  columns=["chief_complaint"],
  dtype=int
 )

 new_patient_df = new_patient_df.reindex(
  columns= x_feature.columns,
  fill_value= 0 
)
 
 return new_patient_df , complaint
