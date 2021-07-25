import boto3
from decouple import config

AWS_ACCESS_KEY_ID     = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
REGION_NAME           = config("REGION_NAME")
INSTANCE_ID           = config("INSTANCE_ID")
INSTANCE_NAME         = config("INSTANCE_NAME")

ec2_client = boto3.client(
    'ec2',
    aws_access_key_id     = AWS_ACCESS_KEY_ID,
    aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
    region_name           = REGION_NAME,
    )

# response = ec2_client.describe_instances()
# for instances in response['Reservations']:
#     print(instances)

ec2_client.create_image( 
    InstanceId=INSTANCE_ID, 
    Name=INSTANCE_NAME, 
    )