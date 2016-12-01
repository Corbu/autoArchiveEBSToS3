# AWS Auto Archive EBS to S3 Lambda Script
# Archives EBS volumes to S3 on instance stop automatically
# created by Cory Burns
# Version 0.0

import boto3

# Variables
region = 'us-east-1' # The region your EC2 instances are in
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

	# Take snapshot of existing EBS Volumes (I don't think there is a way to

	# Create temporary EC2 Instance
	# AWS CLI:
	# aws ec2 run-instances --image-id ami-xxxxxxxx --count 1 --instance-type t2.micro --key-name MyKeyPair --security-group-ids sg-xxxxxxxx 
	
	# This is from the boto3.readthedocs.io page.  Some (most?) of this is probably unneccsesary.  Will need to pair down
	response = client.run_instances(
		DryRun=True|False,
		ImageId='string',
		MinCount=123,
		MaxCount=123,
		KeyName='string',
		SecurityGroups=[
			'string',
		],
		SecurityGroupIds=[
			'string',
		],
		UserData='string',
		InstanceType='t1.micro'|'t2.nano'|'t2.micro'|'t2.small'|'t2.medium'|'t2.large'|'m1.small'|'m1.medium'|'m1.large'|'m1.xlarge'|'m3.medium'|'m3.large'|'m3.xlarge'|'m3.2xlarge'|'m4.large'|'m4.xlarge'|'m4.2xlarge'|'m4.4xlarge'|'m4.10xlarge'|'m4.16xlarge'|'m2.xlarge'|'m2.2xlarge'|'m2.4xlarge'|'cr1.8xlarge'|'r3.large'|'r3.xlarge'|'r3.2xlarge'|'r3.4xlarge'|'r3.8xlarge'|'x1.16xlarge'|'x1.32xlarge'|'i2.xlarge'|'i2.2xlarge'|'i2.4xlarge'|'i2.8xlarge'|'hi1.4xlarge'|'hs1.8xlarge'|'c1.medium'|'c1.xlarge'|'c3.large'|'c3.xlarge'|'c3.2xlarge'|'c3.4xlarge'|'c3.8xlarge'|'c4.large'|'c4.xlarge'|'c4.2xlarge'|'c4.4xlarge'|'c4.8xlarge'|'cc1.4xlarge'|'cc2.8xlarge'|'g2.2xlarge'|'g2.8xlarge'|'cg1.4xlarge'|'p2.xlarge'|'p2.8xlarge'|'p2.16xlarge'|'d2.xlarge'|'d2.2xlarge'|'d2.4xlarge'|'d2.8xlarge'|'f1.2xlarge'|'f1.16xlarge',
		Placement={
			'AvailabilityZone': 'string',
			'GroupName': 'string',
			'Tenancy': 'default'|'dedicated'|'host',
			'HostId': 'string',
			'Affinity': 'string'
		},
		KernelId='string',
		RamdiskId='string',
		BlockDeviceMappings=[
			{
				'VirtualName': 'string',
				'DeviceName': 'string',
				'Ebs': {
					'SnapshotId': 'string',
					'VolumeSize': 123,
					'DeleteOnTermination': True|False,
					'VolumeType': 'standard'|'io1'|'gp2'|'sc1'|'st1',
					'Iops': 123,
					'Encrypted': True|False
				},
				'NoDevice': 'string'
			},
		],
		Monitoring={
			'Enabled': True|False
		},
		SubnetId='string',
		DisableApiTermination=True|False,
		InstanceInitiatedShutdownBehavior='stop'|'terminate',
		PrivateIpAddress='string',
		Ipv6Addresses=[
			{
				'Ipv6Address': 'string'
			},
		],
		Ipv6AddressCount=123,
		ClientToken='string',
		AdditionalInfo='string',
		NetworkInterfaces=[
			{
				'NetworkInterfaceId': 'string',
				'DeviceIndex': 123,
				'SubnetId': 'string',
				'Description': 'string',
				'PrivateIpAddress': 'string',
				'Groups': [
					'string',
				],
				'DeleteOnTermination': True|False,
				'PrivateIpAddresses': [
					{
						'PrivateIpAddress': 'string',
						'Primary': True|False
					},
				],
				'SecondaryPrivateIpAddressCount': 123,
				'AssociatePublicIpAddress': True|False,
				'Ipv6Addresses': [
					{
						'Ipv6Address': 'string'
					},
				],
				'Ipv6AddressCount': 123
			},
		],
		IamInstanceProfile={
			'Arn': 'string',
			'Name': 'string'
		},
		EbsOptimized=True|False
	)
	
		## ** This needs an IAM Role that has access to S3 and can mount/unmount EBS volumes (potentially)
		## The EC2 instance will have a bootstrap script that will:
			### Copy data from the EBS instances to S3
			### Re-mount EBS volumes to original EC2 instance (skip this if using snapshots)
			### Terminate the server

	# If Terminate on Completion is on
		## Terminate original EC2 volume

	# Delete Snapshots

	# Send Email to DevOps