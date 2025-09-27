from pydantic import BaseModel

class PatientData(BaseModel):
    first_name: str
    last_name: str
    identification_number:str
    pregnancles: int
    glucose: int
    bloodpressure: int
    skinthickness: int
    insulin: int
    bmi: float
    diabetespedugreefunction: float
    age: int