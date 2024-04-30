import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.delete_item(
    Key={
       'emp_no': '17248 d'
    }
)
ms = (time.time() - start_time)*(1000)
print("Time taken for single delete: %s" % ms + " ms")