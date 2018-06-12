#!/usr/bin/env python

import boto3

ec2 = boto3.client("ec2")

instances = ec2.describe_instances()
sgs = ec2.describe_security_groups()

instance_sg_set = set()
sg_set = set()

for reservation in instances["Reservations"] :
  for instance in reservation["Instances"]:
    for sg in instance["SecurityGroups"]:
      instance_sg_set.add(sg["GroupName"])


for security_group in sgs["SecurityGroups"] :
  sg_set.add(security_group ["GroupName"])

idle_sg = sg_set - instance_sg_set

print idle_sg
