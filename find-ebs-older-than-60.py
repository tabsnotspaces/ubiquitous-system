#!/usr/bin/env python

import sys
import boto3
import datetime

age = 60

def days_old(date):
    date_obj = date.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

ec2 = boto3.client('ec2')
snapshots = ec2.describe_snapshots()

for snapshot in snapshots['Snapshots']:
    create_date = snapshot['StartTime']
    snapshot_id = snapshot['SnapshotId']
    day_old = days_old(create_date)

    if day_old > age:
        print 'Snapshot ID: ', snapshot_id, 'Created: ', create_date
