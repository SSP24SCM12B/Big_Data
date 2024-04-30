import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
response = table.get_item(
    Key={
        'emp_no': '13000',
    }
)
item = response['Item']
print(item)
ms = (time.time() - start_time)*(1000)
print("Time taken for reading specific: %s" % ms + " ms")