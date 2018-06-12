#!/usr/bin/env python

# imports
import boto3
import sys

ec2 = boto3.resource('ec2', region_name = sys.argv[1])
instance = ec2.Instance(sys.argv[2])
volumes = instance.volumes.all()

for v in volumes:
	for t in v.tags:
		if t['Key']=='Name':
			v_name = t['Value']	
	print 'Name: ', v_name
	print 'ID: ',v.id
	
	
	print 'Attached to: ', v.attachments[0][u'InstanceId']
	print 'Attached Time: ', v.attachments[0][u'AttachTime']
	print 'Attached Device:', v.attachments[0][u'Device']
	print 'Size: ', v.size
	print 'IOPS: ', v.iops
	print '---------------'

