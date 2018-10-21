#!/usr/bin/python
from __future__ import print_function
from rds_helper import RdsHelper
from kms_helper import KmsHelper

region_name = "us-east-1"
project_name = "project123"
pending_window_in_days = 7

rds_helper = RdsHelper(region_name)
kms_helper = KmsHelper(region_name)

# Getting the key
key = kms_helper.describe_key(project_name)

# Deleting the database
rds_helper.delete_database(project_name)
print("Database deleted: %s" % project_name)

# Deleting the key
kms_key = kms_helper.delete_kms_key(key['KeyMetadata']['KeyId'], pending_window_in_days, project_name)
print('Key %s scheduled for deletion in %s days' % (kms_key, pending_window_in_days))
print('Alias alias/%s deleted' % project_name)
