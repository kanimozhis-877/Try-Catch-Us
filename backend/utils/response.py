from bson import ObjectId
from datetime import datetime


def serialize(value):

    if isinstance(
        value,
        ObjectId
    ):

        return str(value)

    if isinstance(
        value,
        datetime
    ):

        return value.isoformat()

    if isinstance(
        value,
        list
    ):

        return [
            serialize(item)
            for item in value
        ]

    if isinstance(
        value,
        dict
    ):

        return {
            key: serialize(val)
            for key, val in value.items()
        }

    return value