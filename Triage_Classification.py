from load_x_y import load_Training_data
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score , confusion_matrix
from patient_inf import new_patient


def patient_Result():

 x_feature , y_target , get_data = load_Training_data()

 x_train , x_test , y_train , y_test = train_test_split(
     x_feature,
     y_target,
     test_size=0.2,
     random_state=42,
     stratify = y_target
 )


 model = LogisticRegression(max_iter=150)
 scaler = StandardScaler()


 x_train = scaler.fit_transform(x_train)
 x_test = scaler.transform(x_test)
 

 model.fit(x_train,y_train)
 prediction = model.predict(x_test)


 cm = confusion_matrix(y_test,prediction)
 accuracy = accuracy_score(y_test,prediction)

 patient , complaint  = new_patient()


 patient = scaler.transform(patient)


 Result_print = model.predict(patient)

 
 return Result_print , complaint
