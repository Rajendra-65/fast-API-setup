from fastapi import FastAPI,Path,HTTPException,Query;
import json;

app = FastAPI()

def load_data () : 
    with open('patients.json','r') as f:
        data = json.load(f)

    return data

@app.get("/")
def hello():
    return {
        'message' : 'Patient Management System API'
    }

@app.get("/about")

def about() : 
    return {
        'message' : "A fully functional API to manage your patient records"
    }

# get route
@app.get("/view")

def view() : 
    data = load_data()

    return data

@app.get('/patient/{patient_id}')

def view_patient (patient_id : str = Path(..., description = "Id of the patient in the DB", example = "p001")) :
    # load all patient
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code = 404 , detail = "patient not found")

@app.get('/sort')

def sort_patient(
    sort_by: Literal["height", "weight", "bmi"] = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: Literal["asc", "desc"] = Query("asc", description="Sort in ascending or descending order")
):
    return {"sort_by": sort_by, "order": order}


