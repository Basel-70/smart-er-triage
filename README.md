# Smart ER Triage 🏥

A command-line emergency room triage assistant. It takes a patient's vital signs and chief complaint, predicts their **ESI (Emergency Severity Index) level** with a machine learning model, lists the available doctors for that complaint, and announces high-priority instructions out loud using the **HUMAIN Voice** text-to-speech API.

## Features

- **ESI prediction**: a Logistic Regression model (scikit-learn) trained on ~55,000 ER encounters predicts a risk level from 1 (highest) to 5 (lowest).
- **Guided patient intake**: prompts for age, sex, blood pressure, heart rate, respiratory rate, temperature, SpO₂ and pain score, with autocomplete for the chief complaint.
- **Doctor matching**: maps each complaint to a specialty and shows the doctors currently marked `Available`.
- **Emergency fast path**: critical cases (unresponsive, cardiac arrest, massive hemorrhage, ongoing seizure, severe respiratory distress) skip the model and go straight to priority 1.
- **Voice announcements**: high-risk and emergency cases are announced through the speakers using HUMAIN Voice.

## How it works

```
System_Build.py  (main menu)
 ├─ 1. New patient
 │    └─ Triage_Classification.py  → trains the model, predicts ESI level
 │         ├─ load_x_y.py          → loads training data from triage_Data.db
 │         └─ patient_inf.py       → collects the new patient's data
 │    └─ doctor_selection.py       → lists available doctors for the complaint
 │    └─ humain_voice_tts.py       → speaks the alert if ESI < 3
 └─ 2. Emergency patient           → priority 1 + voice alert
```

## Project files

| File | Purpose |
|---|---|
| `System_Build.py` | Entry point: main menu and program flow |
| `Triage_Classification.py` | Trains the Logistic Regression model and predicts the patient's ESI level |
| `patient_inf.py` | Collects a new patient's vitals and chief complaint |
| `load_x_y.py` | Loads patient (training) and doctor data from the SQLite database |
| `doctor_selection.py` | Complaint → specialty mapping and available-doctor lookup |
| `humain_voice_tts.py` | Text-to-speech using the HUMAIN Voice API |
| `read_data_and_transfer.py` | Imports `Doctor_Data.csv` into the `Doctor` table of the database |
| `triage_Data.db` | SQLite database with the `patients` and `Doctor` tables |
| `data_triage.csv` | Raw ER triage dataset (vitals, labs, complaints, ESI level) |
| `Doctor_Data.csv` | Doctor roster: specialty, room, availability, shift |

> All files are kept in the project root because the scripts import each other and open `triage_Data.db` by relative path.

## Getting started

**Requirements:** Python 3.9+ and a working audio output device.

```bash
git clone https://github.com/Basel-70/smart-er-triage.git
cd smart-er-triage
pip install -r requirements.txt
```

Then set up HUMAIN Voice (SDK and API key) as described in [Powered by HUMAIN Voice](#powered-by-humain-voice).

**Run:**

```bash
python System_Build.py
```

Then choose:

- `1` to add a new patient and get their ESI level and available doctors
- `2` for an emergency patient
- `0` to exit

To reload the doctor roster after editing `Doctor_Data.csv`:

```bash
python read_data_and_transfer.py
```

## Powered by HUMAIN Voice

<p align="center">
  <a href="https://www.humain.com">
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/HUMAIN.svg" alt="HUMAIN" width="260">
  </a>
</p>

The spoken alerts in this project use **HUMAIN Voice**, the text-to-speech service from [HUMAIN](https://www.humain.com), Saudi Arabia's AI company. Instead of only printing instructions on the screen, the system speaks them out loud, so a patient in the waiting area hears what to do even if they aren't looking at the screen.

### How it's used

All the voice logic lives in a single function, `speak(text)`, in `humain_voice_tts.py`:

1. **Connect**: creates a `TTSClient` with the API key and the endpoint `https://api.voice.humain.com`.
2. **Pick a voice**: fetches the list of available voices and selects the one whose label contains `mul_abdullah`.
3. **Synthesize**: sends the text to the **Nebula** model (`TtsModel.Nebula`), which returns raw audio (16-bit PCM).
4. **Play**: converts the audio to a NumPy array and plays it at **24 kHz** through the speakers with `sounddevice`, waiting until it finishes.
5. **Close**: closes the client connection.

```python
from humain_voice_tts import speak

speak("Please remain where you are. A nurse will assist you shortly.")
```

### When the system speaks

| Situation | Spoken message |
|---|---|
| Predicted ESI level is 1 or 2 (high risk) | "Please remain where you are. A nurse will assist you shortly." |
| Emergency patient (menu option 2) | "Your case has been registered as an emergency. Please ask the nearest nurse for immediate assistance." |
| User exits the program | "Thank you. Your assessment is now complete." |

### Setup

1. Get an API key from HUMAIN.
2. Install the `humain_voice` SDK following HUMAIN's instructions (it isn't on PyPI).
3. In `humain_voice_tts.py`, replace the `"HUMAIN_API_KEY"` placeholder with your key. Don't commit your real key.
4. Make sure your computer has a working audio output device.

## Tech stack

Python · pandas · scikit-learn · SQLite · prompt_toolkit · HUMAIN Voice · sounddevice · NumPy

## Disclaimer

This is an educational project and is not a medical device. It must not be used to make real clinical decisions. The doctor names and data are synthetic.

## Author

**Basel Zahrani** · [GitHub](https://github.com/Basel-70) · [LinkedIn](https://www.linkedin.com/in/basel-al-zahrani-b1a0b2339/)
