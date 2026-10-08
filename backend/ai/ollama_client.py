import requests

from app.config import (
    OLLAMA_URL,
    OLLAMA_MODEL
)


def ask_ollama(
    prompt: str
):

    try:

        response = requests.post(

            OLLAMA_URL,

            json={

                "model":
                    OLLAMA_MODEL,

                "prompt":
                    prompt,

                "stream":
                    False
            },

            timeout=120
        )


        response.raise_for_status()


        data = response.json()


        return data.get(
            "response",
            "No AI response generated."
        )


    except Exception as error:

        return (
            "AI service is currently "
            "unavailable. "
            f"Please review the reports manually. "
            f"Reason: {error}"
        )