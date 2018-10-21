#!/usr/bin/python
from __future__ import print_function
from rds_helper import RdsHelper
from kms_helper import KmsHelper

region_name = "us-east-1"
rds_helper = RdsHelper(region_name)
kms_helper = KmsHelper(region_name)

# Project name
project_name = "project123"

# Creating the Key
policy = open("example-kms-policy.json").read()
kms_key = kms_helper.create_kms_key(project_name, region_name, policy, True)
print('Created CMK KeyId:', kms_key['KeyMetadata']['KeyId'])
print("Alias created: alias/%s" % project_name)

# Creating the database
az_name = 'us-east-1a'
db_instance_class = "db.t2.small"
retention_period = 7
master_username = "CHANGE_ME"
master_password = "CHANGE_MY_PASS"

rds_helper.create_postgres_database(project_name, db_instance_class, az_name,
    retention_period, kms_key, master_username, master_password)

print("Database created: %s" % project_name)
