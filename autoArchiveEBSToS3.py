# AWS Auto Archive EBS to S3 Lambda Script
# Archives EBS volumes to S3 on instance stop automatically
# created by Cory Burns
# Version 0.1

import boto3

# Variables
region = 'us-east-1' # The region your EC2 instances are in
availabilityZone = 'us-east-1a' # The availability zone the stopped instance is in, this will be pulled from the cloudwatch data hopefully
ami = 'ami-b73b63a0' # The default Linux AMI.  Keep this updated
## S3 Bucket
## Terminate original EC2 instance on completion #Off by default
## Include AutoScale #Off by default?
## Include Last AutoScale #On by default

# Script
def lambda_handler(event, context):
	# Get Stopped EC2 instance ID
		## Verify it was not stopped by AutoScale
		## Verify it is not a temp EC2 instance (created by this very script)
		## Get list of attached EBS Volumes

	# Take snapshot of existing EBS Volumes
	# Might not need to take a snapshot

	# Create temporary EC2 Instance
	# AWS CLI:
	# aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-xxxxxxxx 
	
	# This is from the boto3.readthedocs.io page.  I think I have this paired down to what I need, I just need to turn these into
	# variables that make sense...and figure out the EBS syntax specifically
	# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.run_instances
	client = boto3.client('ec2')
	response = client.run_instances(
		ImageId=ami, # Required, this will be replaced with a variable
		MinCount=1, # Required
		MaxCount=1, # Required
		# SecurityGroups=[ # This will be replaced with a variable
		#	'string', # For Default VPCs
		#],
		#SecurityGroupIds=[
		#	'string', # For non-default VPCs 
		#],
		# The temp EC2 instance will have a bootstrap script that will:
			## Unmount the EBS instances from the original EC2 instance
			## Mount the EBS instances on the temp EC2 instance
			## Copy data from the mounted EBS instances to the appropriate S3 bucket
			## Re-mount EBS volumes to original EC2 instance
			## Shutdown the server (which will terminate the instance as per the below settings)
		# UserData='string', # This should also be replaced with a variable
		InstanceType='t2.micro', # Required
		Placement={
			'AvailabilityZone': availabilityZone
		},
		BlockDeviceMappings=[
			{
				'DeviceName': '/dev/xvda',
				'Ebs': {
					# 'SnapshotId': 'string',
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

	# If Terminate on Completion is on
		## Terminate original EC2 volume

	# Delete Snapshots

	# Send Email to DevOps