import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

table.put_item(
   Item={
        'emp_no': '100001',
        'first_name': 'Jane',
        'last_name': 'Doe',
        'birth_date': '1956-11-14',
        'gender': 'M',
        'hire_date': '1988-02-26',
        'salary': '55000',
        'title':'Staff',
        'dept_no':'d009',
        'dept_name': 'Customer Service'

    }
)

ms = (time.time() - start_time)*(1000)
print("Time taken for single insertion: %s" % ms + " ms")