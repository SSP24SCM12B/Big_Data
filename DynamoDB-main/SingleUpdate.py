import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.update_item(
    Key={
        'emp_no': '100001',
    },
    UpdateExpression='SET last_name = :val1',
    ExpressionAttributeValues={
        ':val1': 'Kadiya'
    }
)
response = table.get_item(
    Key={
        'emp_no': '100001',
    }
)
item = response['Item']
print(item)


ms = (time.time() - start_time)*(1000)
print("Time taken for single update: %s" % ms + " ms")