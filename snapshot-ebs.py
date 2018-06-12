#!/usr/bin/env python

import boto3
import sys

ec2 = boto3.resource('ec2')
instance = ec2.Instance(sys.argv[1])
description = raw_input("Snapshot Description: ")
for device in instance.block_device_mappings:
    ec2.create_snapshot(Description=description,
        VolumeId=device.get('Ebs').get('VolumeId'))
