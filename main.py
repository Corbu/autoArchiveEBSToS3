# AWS Auto Archive EBS to S3 Lambda Script
# Archives EBS volumes to S3 on instance stop automatically
# created by Cory Burns
# Version 0.1

import aa_ec2

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
	aa_ec2.createEC2(ami, availabilityZone)

	# If Terminate on Completion is on
		## Terminate original EC2 volume

	# Delete Snapshots

	# Send Email to DevOps