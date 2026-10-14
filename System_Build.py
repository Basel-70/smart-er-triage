import pandas as pd
from Triage_Classification import patient_Result
from doctor_selection import available_Doctor
from humain_voice_tts import speak

def print_Menu():
 print("")
 print("     𓂃˖˳·˖ ִֶָ ⋆🌷͙⋆ ִֶָ˖·˳˖𓂃 ִֶָ  ")
 print("")
 print("1️⃣    Add new patient choose ✏️ : ")
 print("")
 print("2️⃣    Emergency patient 🚨 : ")
 print("")
 print("🅾️    To exit choose ➜🚪 : ")
 print("")
 return

def print_Emergency_menu():
 print("  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️  ⚠️")
 print("")
 print("1️⃣    Unresponsive : ")
 print("")
 print("2️⃣    Cardiac arrest : ")
 print("")
 print("3️⃣    Massive hemorrhage : ")
 print("")
 print("4️⃣    Seizure ongoing : ")
 print("")
 print("5️⃣    Severe respiratory distress : ")
 return

user = 3

while user != 0:

 print_Menu()

 user = int(input())

 if user == 1:
  risk , complaint = patient_Result()
  print("Risk level from highest risk (1) to lowest risk (5):", risk)

  if risk <3:

   speak("Please remain where you are. A nurse will assist you shortly.")
   print("Priority Level: High. A nurse will assist you and take you to the appropriate doctor as soon as possible.")
  
  print("")
  print("Available doctors for your complaint:", complaint)
  print("")
  print(available_Doctor(complaint).to_string(index=False))

 elif user == 2:
  print_Emergency_menu()
  print("")
  emergency_user = int(input())

  if emergency_user in (1, 2, 3, 4, 5):
   print("")
   print("Priority Level 🚨 : 1")

   speak("Your case has been registered as an emergency. Please ask the nearest nurse for immediate assistance.")   
   print("Action: Immediate medical attention required ⛨.")

speak("Thank you. Your assessment is now complete.")
print("Thank you. Your assessment is complete. Please follow the instructions provided and wait for assistance if needed.")

 


 
 

  
  



 
