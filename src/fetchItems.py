import json
import boto3

def fetch_items(event):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('ItemTable')

    try:
        response = table.scan()
        items = response.get('Items')

    except Exception as e:
        print(e)
        items = None

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
"""
In this code, we import the necessary modules, set up the AWS SDK, and define the fetch_items function. 
The function connects to the DynamoDB table named 'ItemTable', performs a scan operation to retrieve all items, 
and stores them in the items variable. If an exception occurs, it is caught and the items variable is set to None. 
Finally, the function returns a response with a status code of 200 and the items in the response body, serialized as JSON.

"""
