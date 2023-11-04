import json


def newapi(event, context):
    body = {
        "message": "my new API!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response