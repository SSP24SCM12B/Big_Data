import boto3
import time
start_time = time.time()
# Get the service resource.

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

item_1 = {"emp_no":"10037"}
item_2 = {"emp_no":"10038"}
item_3 = {"emp_no":"10039"}
item_4 = {"emp_no":"10040"}
item_5 = {"emp_no":"10041"}
item_6 = {"emp_no":"10042"}
item_7 = {"emp_no":"10043"}
item_8 = {"emp_no":"10044"}
item_9 = {"emp_no":"10045"}
item_10 = {"emp_no":"10046"}
item_11 = {"emp_no":"10047"}



items_to_delete = [item_1, item_2,item_3,item_4,item_5,item_6,item_7,item_8,item_9,item_10,item_11]

with table.batch_writer() as batch:
    for item in items_to_delete:
        response = batch.delete_item(Key={
            "emp_no": item["emp_no"],
        })
ms = (time.time() - start_time)*(1000)
print("Time taken for multiple delete: %s" % ms + " ms")