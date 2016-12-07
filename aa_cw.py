 # aa_cw.py
 # CloudWatch functions
 
import boto3
import json

def getInstanceID(event):
	return json.loads(json.dumps(event))['detail']['instance-id']
	
def lambda_handler(event, context):
    id = getInstanceID(event)
    return id