import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('studentData')

def lambda_handler(event, context):
    student_id = event['studentid']
    name = event['name']
    student_class = event['class']
    age = event['age']
    
    response = table.put_item(
        Item={
            'studentid': student_id,
            'name': name,
            'class': student_class,
            'age': age
        }
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Student data saved successfully!')
    }
