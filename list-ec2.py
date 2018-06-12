#!/usr/bin/env python

# imports
import boto3
import sys

ec2 = boto3.resource('ec2', region_name = sys.argv[1])

#filter values

filters = [
	{
		'Name': 'instance-state-name',
		'Values': ['running']
	}
]
	
instances = ec2.instances.filter(Filters=filters)
	
for i in instances:
	for t in i.tags:
		if 'Name' in t['Key']:
			name = t['Value']
	print 'Name: ', name
	print 'Instance ID: ', i.id
	print 'Private IP: ', i.private_ip_address
	print 'Launch Time: ', i.launch_time
	print '-------------------------'
