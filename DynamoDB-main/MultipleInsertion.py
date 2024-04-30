import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

with table.batch_writer() as batch:
    batch.put_item(
        Item={
            'emp_no': '100002',
            'first_name': 'Bhaktiben',
            'last_name': 'Kadiya',
            'birth_date': '1999-11-14',
            'gender': 'F',
            'hire_date': '2020-02-26',
            'salary': '55000',
            'title':'Software Engineer',
            'dept_no':'d009',
            'dept_name': 'Customer Service'
            }

    )
    batch.put_item(
        Item={
            'emp_no': '100003',
            'first_name': 'Shraddha',
            'last_name': 'Kadiya',
            'birth_date': '1998-11-14',
            'gender': 'F',
            'hire_date': '2019-02-26',
            'salary': '55000',
            'title':'Staff',
            'dept_no':'d009',
            'dept_name': 'Customer Service'
        }
    )
    batch.put_item(
        Item={
            'emp_no': '100004',
            'first_name': 'Devadas',
            'last_name': 'Challa',
            'birth_date': '1956-11-14',
            'gender': 'M',
            'hire_date': '1988-02-26',
            'salary': '55000',
            'title':'Staff',
            'dept_no':'d009',
            'dept_name': 'Customer Service'
        }
    )
    batch.put_item(
        Item={
            'emp_no': '100005',
            'first_name': 'Shashank',
            'last_name': 'Bommadevara',
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