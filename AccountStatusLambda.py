import json

# 1 Import boto3 and create client connection with DynamoDB - Link to documentation - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb/client/get_item.html
import boto3

client = boto3.client("dynamodb")


def lambda_handler(event, context):
    print(f"This is the input from agent{event}")
    account_id = event["parameters"][0]["value"]
    response = client.get_item(
        TableName="customerAccountStatus", Key={"AccountID": {"N": account_id}}
    )
    # printing response from dynamoDB
    print(response)
    # This response format is based on aws docs - https://docs.aws.amazon.com/bedrock/latest/userguide/agents-lambda.html
    response_body = {"application/json": {"body": json.dumps(response)}}

    action_response = {
        "actionGroup": event["actionGroup"],
        "apiPath": event["apiPath"],
        "httpMethod": event["httpMethod"],
        "httpStatusCode": 200,
        "responseBody": response_body,
    }

    session_attributes = event["sessionAttributes"]
    prompt_session_attributes = event["promptSessionAttributes"]

    api_response = {
        "messageVersion": "1.0",
        "response": action_response,
        "sessionAttributes": session_attributes,
        "promptSessionAttributes": prompt_session_attributes,
    }
    print("api_response: ", api_response)
    return api_response
