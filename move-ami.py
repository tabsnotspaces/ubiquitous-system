#!/usr/bin/env python

import boto3
import sys

srcRegion = raw_input("Source Region: ")
destRegion = raw_input("Destination Region: ")
amiID = raw_input("AMI ID: ")
amiName = raw_input("New AMI Name: ")

ec2 = boto3.client('ec2', region_name = destRegion)

ami = ec2.copy_image(
    Name = amiName,
    SourceImageId = amiID,
    SourceRegion = srcRegion
)
