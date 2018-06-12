#!/usr/bin/env python

import boto3
import sys

instanceName = raw_input("Instance ID: ")
ami_Name = raw_input("AMI Name: ")
ami_Description = raw_input("AMI Description: ")

ec2 = boto3.client('ec2')

ami = ec2.create_image(
    Description = ami_Description,
    InstanceId = instanceName,
    Name = ami_Name
)
