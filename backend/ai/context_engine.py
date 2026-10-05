from database.mongodb import db

def build_context(patient_id):
    patient=db.patients.find_one({"patient_id":patient_id}) or db.patients.find_one({"_id":patient_id})
    reports=list(db.reports.find({"patient_id":patient_id}).sort("created_at",-1).limit(10))
    labs=list(db.lab_results.find({"patient_id":patient_id}).sort("created_at",-1).limit(20))
    def clean(x):
        x=dict(x); x.pop("_id",None); return x
    return {"patient":clean(patient) if patient else None,"reports":[clean(x) for x in reports],"lab_results":[clean(x) for x in labs]}
