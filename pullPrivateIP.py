#!/usr/bin/env python

# imports
import boto3
import sys
import subprocess

ec2 = boto3.resource('ec2', region_name = sys.argv[1])
instance = ec2.Instance(sys.argv[2])
#filter values

private_ip = instance.public_ip_address
command = "echo 'this is a test' >> /tmp/test"
username = "ec2-user"
user_host = username + "@" + private_ip
ssh = subprocess.Popen(["ssh", "%s" % user_host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
