import boto3

import json

region = 'eu-west-1'

instances = ['instance-id']

def lambda_handler(event,context):
    ec2 = boto3.client('ec2', region_name=region)
    ec2.stop_instances(InstanceIds=instances)
    
    return {
        'statusCode': 200,
        'body':json.dumps('Lanzar tus instancias:' + str(instances))
    }
