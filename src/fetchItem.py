import json
import boto3

def fetch_item(event, context):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    item_id = event['pathParameters']['id']

    try:
        response = table.get_item(Key={'id': item_id})
        item = response.get('Item')

    except Exception as e:
        print(e)
        item = None

    return {
        'statusCode': 200,
        'body': json.dumps(item)
    }

"""
In this code, we use the boto3 library to interact with AWS services. 
The fetch_item function receives the event and context parameters, 
similar to the AWS Lambda handler function. It retrieves the id from the 
pathParameters of the event object, connects to the DynamoDB table named 'ItemTable', 
and retrieves the item with the given id. Finally, it returns a response with a status c
ode of 200 and the item in the response body.

Please note that in Python, you don't need to use "use strict"; as Python is a dynamically typed language.

"""
