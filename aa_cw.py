# aa_cw.py
# Functions regarding the JSON details from the CloudWatch event
 
import boto3
import json

def getInstanceID(event):
	"""Grabs the EC2 Instance ID from the CloudWatch JSON
	event = the JSON event passed through lambda_handler(event, context)"""
	return json.loads(json.dumps(event))['detail']['instance-id']

def lambda_handler(event, context):
	id = getInstanceID(event)
	volumes = returnEBS(id)
	return volumes