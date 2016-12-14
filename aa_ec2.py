# aa_ec2.py
# Functions regarding EC2 instance manipulation

import boto3

def createEC2(ami,availabilityZone,vpc,userData,iamRole):
	"""Creates a temporary EC2 instance that mounts all EBS volumes from a stopped EC2 instance and stores them in S3
	ami = Typically this will be the default AWS Linux AMI
	availabilityZone = the availability zone the EC2 instance will be created in"""
	
	# This was mostly pulled from the BOTO3 docs page:
	# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.run_instances
	client = boto3.client('ec2')
	
	response = client.run_instances(
		ImageId=ami, # The AMI of the EC2 Instance
		# We only want one instance created
		MinCount=1,
		MaxCount=1,
		SecurityGroupIds=[vpc] # The VPC that this will run in
		# The temp EC2 instance will have a bootstrap script that will:
			## Unmount the EBS instances from the original EC2 instance
			## Mount the EBS instances on the temp EC2 instance
			## Copy data from the mounted EBS instances to the appropriate S3 bucket
			## Re-mount EBS volumes to original EC2 instance
			## Shutdown the server (which will terminate the instance as per the below settings)
		UserData=userData,
		InstanceType='t2.micro', # You can change this if neccessary, but a t2 micro should be sufficient
		Placement={
			'AvailabilityZone': availabilityZone # The availability zone the EC2 Instance is going to be placed in
		},
		# We just need a small default EBS volume for the OS
		BlockDeviceMappings=[
			{
				'DeviceName': '/dev/xvda',
				'Ebs': {
					'VolumeSize': 8,
					'DeleteOnTermination': True,
					'VolumeType': 'gp2',
				},
			},
		],
		Monitoring={
			'Enabled': False # Required
		},
		InstanceInitiatedShutdownBehavior='terminate', # We don't want this to stick around once the copying is done
		#IamInstanceProfile={ # ** This needs an IAM Role that has access to S3 and can mount/unmount EBS volumes (potentially)
		#	'Arn': 'string',
		#	'Name': 'string'
		#},
	)

def returnEBS(id, root):
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

def returnAZ(id):
	"""Returns the Availability Zone of an EC2 instance
	id = Instance ID"""
	
	ec2 = boto3.resource('ec2')
	return ec2.Instance(id).placement['AvailabilityZone']

def returnOS(id):
	"""Returns the OS of an EC2 instance.
	id = Instance ID"""
	
	ec2 = boto3.resource('ec2')
	
	# Platform only returns Windows or blank
	if ec2.Instance(id).platform != 'Windows':
		return 'Linux'
	else:
		return ec2.Instance(id).platform

def returnVPC(id):
	"""Returns the VPC of an EC2 instance
	id = Instance ID"""
	
	ec2 = boto3.resource('ec2')
	return ec2.Instance(id).vpc_id


def lambda_handler(event, context):
	id = getInstanceID(event)
	volumes = returnEBS(id, '1')
	az = returnAZ(id)
	os = returnOS(id)
	vpc = returnVPC(id)
	
	return volumes, az, os, vpc

