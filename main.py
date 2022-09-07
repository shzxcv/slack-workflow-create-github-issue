import json
import os

def token_validator(token):
    verification_token = os.getenv('verification_token')
    return True if token == verification_token else False

def handler(event, _):
    body = json.loads(event['body'])
    if token_validator(body['token']):
        return {
            "statusCode": 200,
            "challenge": body['challenge']
        }
    else:
        return {
            "statusCode": 500
        }
