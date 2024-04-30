import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
response = table.scan()
data = response['Items']
while 'LastEvaluatedKey' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extend(response['Items'])

ms = (time.time() - start_time)*(1000)
print("Time taken for reading all data: %s" % ms + " ms")