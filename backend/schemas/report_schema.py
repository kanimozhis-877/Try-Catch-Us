from pydantic import BaseModel


class ReportCreate(BaseModel):

    patient_id: str

    report_type: str

    title: str

    content: str = ""

    notes: str = ""

    file_name: str = ""

    report_date: str | None = None