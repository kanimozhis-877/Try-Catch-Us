from database.mongodb import db


def generate_patient_id():

    count = db.patients.count_documents({})

    number = count + 1

    while db.patients.find_one(
        {"patient_id": f"LL{number:04d}"}
    ):

        number += 1

    return f"LL{number:04d}"