# AWS Auto Archive EBS to S3 Lambda Script
# Archives EBS volumes to S3 on instance stop automatically
# created by Cory Burns
# Version 0.0

# Variables
## S3 Bucket
## Terminate on completion
## Include AutoScale
## Include Last AutoScale

# Script

# Get Stopped EC2 instance ID
## Verify it was not stopped by AutoScale
## Verify it is not a temp EC2 instance (created by this very script)
## Get list of attached EBS Volumes

# Take snapshot of existing EBS Volumes (I don't think there is a way to

# Create temporary EC2 Instance
## ** This needs an IAM Role that has access to S3 and can mount/unmount EBS volumes (potentially)
## The EC2 instance will have a bootstrap script that will:
### Copy data from the EBS instances to S3
### Re-mount EBS volumes to original EC2 instance (skip this if using snapshots)
### Terminate the server

# If Terminate on Completion is on
## Terminate original EC2 volume

# Delete Snapshots

# Send Email to DevOps