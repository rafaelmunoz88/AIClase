import pickle

import numpy as np
from schemas.diabetes_schemas import PatientData

with open('RFDiabetesv132.pkl','rb') as file:
    model = pickle.load(file)

labels = ["sano","Emfermo"]

def diabetes_prediction(data: PatientData):

    
    xin = np.array([
        data.pregnancles,
        data.glucose,
        data.bloodpressure,
        data.skinthickness,
        data.insulin,
        data.bmi,
        data.diabetespedugreefunction,
        data.age
    ]).reshape(1,8)

    prediction = model.predict(xin)
    print("prediction ", prediction)
    return labels[prediction[0]]

