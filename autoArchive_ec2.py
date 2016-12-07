# autoArchive_ec2.py
# Creates a new EC2 instance

# AWS CLI:
# aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-xxxxxxxx 
	
# This is from the boto3.readthedocs.io page.  I think I have this paired down to what I need, I just need to turn these into
# variables that make sense...and figure out the EBS syntax specifically
# http://boto3.readthedocs.io/en/latest/reference/services/ec2.html#EC2.Client.run_instances

def createEC2(ami,availabilityZone):
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
