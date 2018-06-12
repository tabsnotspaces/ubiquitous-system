#!/usr/bin/python

import boto3
import sys

elbList = boto3.client('elb')
ec2 = boto3.resource('ec2')
elbName = sys.argv[1]


bals = elbList.describe_load_balancers(LoadBalancerNames=[elbName])
for elb in bals['LoadBalancerDescriptions']:
    for ec2Id in elb['Instances']:
        running_instances = \
            ec2.instances.filter(Filters=[{'Name': 'instance-state-name'
                                 , 'Values': ['running']},
                                 {'Name': 'instance-id',
                                 'Values': [ec2Id['InstanceId']]}])
        for instance in running_instances:
            print 'Instance : ', instance.id, "Private IP: ", instance.private_ip_address
