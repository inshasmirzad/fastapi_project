# models.py
from pydantic import BaseModel
from enum import Enum

class GenderEnum(str, Enum):
    male = "Male"
    female = "Female"

class PatientBaseModel(BaseModel):
    name: str
    age: int
    gender: GenderEnum
    sugar_level: int
    medical_history: str
    prescriptions: str
    lab_results: str
