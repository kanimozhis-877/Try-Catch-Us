import secrets
def generate_patient_id(): return "PAT-" + secrets.token_hex(4).upper()
