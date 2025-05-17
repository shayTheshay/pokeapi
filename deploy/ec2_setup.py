import boto3
import os

from dotenv import load_dotenv 
from .security_group_setup import get_security_group_id

load_dotenv()

def get_instance():
    print("getting the instance of ec2, available")
    

def create_instance():

    sg_id = get_security_group_id()

    ec2 = boto3.resource('ec2', region_name=os.getenv("REGION-NAME"))

    instance = ec2.create_instances(
        ImageId=os.getenv("IMAGE_ID"),  # Replace with Ubuntu AMI
        MinCount=1,
        MaxCount=1,
        InstanceType=os.getenv("INSTANCE_TYPE"),
        KeyName=os.getenv("KEY_PAIR_NAME"),
        SecurityGroupIds=[sg_id],  # Open port 22 and 8000
        UserData=open('deploy/setup_script.sh').read(),   # We'll define this below
        TagSpecifications=[{
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'pokeapi-server'}]
        }]
    )[0]
    print("Launched:", instance.id)