# aa_cw.py
# Functions regarding the JSON details from the CloudWatch event
 
import boto3
import json

def getInstanceID(event):
	"""Grabs the EC2 Instance ID from the CloudWatch JSON
	event = the JSON event passed through lambda_handler(event, context)"""
	return json.loads(json.dumps(event))['detail']['instance-id']
	
def returnEBS(id, root=1):
	"""Outputs all the attached EBS volumes of an instance
	id = the Instance ID
	root = include the root volume.  0 no, 1 yes.  Defaults to yes"""
	ec2 = boto3.resource('ec2')
	volume_id_list = []
	
	volumes = ec2.Instance(id).volumes.all()
	
	if root==0:
		block_devices = ec2.Instance(id).block_device_mappings
		
		# Get the root volume ID
		for b in block_devices:
			print b['DeviceName']
			print b['Ebs']['VolumeId']
			if b['DeviceName'] == ec2.Instance(id).root_device_name:
				root_volume = b['Ebs']['VolumeId']

		# Get the list of EBS volumes attached, except for the root volume
		for v in volumes:
			if v.id != root_volume:
				volume_id_list.append(v.id)
	else:
		for v in volumes:
			volume_id_list.append(v.id)
		
	return volume_id_list

def lambda_handler(event, context):
	id = getInstanceID(event)
	volumes = returnEBS(id)
	return volumes