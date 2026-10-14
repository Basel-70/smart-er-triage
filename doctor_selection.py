import pandas as pd
import sqlite3
from load_x_y import load_Doctor_data

complaint_to_specialty = {

    "Moderate abdominal pain": "General Medicine",

    "Laceration requiring sutures": "Emergency Medicine",

    "Back pain": "Orthopedics",

    "Vomiting": "General Medicine",

    "Headache severe": "Neurology",

    "Fever": "General Medicine",

    "Minor injury": "Orthopedics",

    "Cough": "Pulmonology",

    "Cold symptoms": "General Medicine",

    "Sprain": "Orthopedics",

    "Rash": "Dermatology",

    "Mild abdominal discomfort": "General Medicine",

    "Stroke symptoms": "Emergency Medicine",

    "Severe abdominal pain": "Emergency Medicine",

    "High fever with confusion": "Emergency Medicine",

    "Severe shortness of breath": "Emergency Medicine",

    "Chest pain": "Emergency Medicine",

    "Head injury with LOC": "Emergency Medicine",

    "Medication question": "General Medicine",

    "Follow-up visit": "General Medicine",

    "Minor rash": "Dermatology",

    "Prescription refill": "General Medicine",

    "Chronic pain stable": "Internal Medicine",

    "Unresponsive": "Emergency Medicine",

    "Cardiac arrest": "Emergency Medicine",

    "Massive hemorrhage": "Emergency Medicine",

    "Seizure ongoing": "Emergency Medicine",

    "Severe respiratory distress": "Emergency Medicine"
 }


def available_Doctor(complaint):

 get_data = load_Doctor_data()


 specialty = complaint_to_specialty.get(complaint)


 available_doctors = get_data[(get_data["specialty"] == specialty) & (get_data["availability"] == "Available")]

 return available_doctors


