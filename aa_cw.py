# aa_cw.py
# Functions regarding the JSON details from the CloudWatch event
 
import boto3
import json

def getInstanceID(event):
	"""Grabs the EC2 Instance ID from the CloudWatch JSON"""
	return json.loads(json.dumps(event))['detail']['instance-id']
	
def returnEBS(id):
	"""Outputs all the attached EBS volumes of an instance"""
	ec2 = boto3.resource('ec2')
	volume_id_list = []
	
	volumes = ec2.Instance(id).volumes.all()
	
	for v in volumes:
		volume_id_list.append(v.id)
		
	return volume_id_list

def lambda_handler(event, context):
	id = getInstanceID(event)
	volumes = returnEBS(id)
	return volumes