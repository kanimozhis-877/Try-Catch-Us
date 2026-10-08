from ai.context_engine import (
    build_context
)

from ai.ollama_client import (
    ask_ollama
)


def analyze(
    patient_id,
    question
):

    context = build_context(
        patient_id
    )


    prompt = f"""

You are LIFE LINK,
a clinical decision-support assistant.

You must NOT diagnose a patient
or prescribe treatment.

Review the available patient information
and provide:

1. Important observations
2. Report trends
3. Missing information
4. Possible concerns for doctor review
5. Questions a doctor may consider

Patient context:

{context}

Doctor question:

{question}

Always state that the final clinical
decision must be made by a qualified
healthcare professional.
"""


    answer = ask_ollama(
        prompt
    )


    return {

        "patient_id":
            patient_id,

        "answer":
            answer,

        "disclaimer":
            "AI output is decision support only. A qualified healthcare professional must verify all findings."
    }