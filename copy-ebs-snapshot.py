#!/usr/bin/env python

import boto3
import sys

srcRegion = raw_input("Source Region: ")
destRegion = raw_input("Destination Region: ")
snapID = raw_input("Snapshot ID: ")
snapName = raw_input("New Snapshot Description: ")

ec2 = boto3.client('ec2', region_name = destRegion)

snap = ec2.copy_snapshot(
    Description = snapName,
    SourceSnapshotId = snapID,
    SourceRegion = srcRegion
)

print snap
