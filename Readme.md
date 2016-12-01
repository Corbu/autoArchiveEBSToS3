autoArchiveEBStoS3.py

This is a small Lambda script that can be used to automatically archive EBS volumes to S3.
It is designed to be used in scenarios where

A) You don't have access to the EC2 instances (due to not having the appropriate key pairs or passwords)
B) You want to (either temporarily or permanently) store EBS data after an EC2 instance is stopped in S3 rather than use a snapshot
C) You don't want to do this yourself

This script will (hopefully) differentiate between EBS volumes created and destroyed by AutoScaling

This is my first attempt at a lambda script or any real IAAS programming so it will probably suck or not work right

Enjoy