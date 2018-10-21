#!/usr/bin/python
from __future__ import print_function
import boto3

class KmsHelper:
    """KmsHelper class"""

    def __init__(self, region_name):
        self.kms_client = boto3.client('kms', region_name=region_name)

    def describe_key(self, alias):
        ''' Retrieve and describe a key from KMS '''
        response = self.kms_client.describe_key(KeyId="alias/" + alias)
        return response

    def delete_kms_key(self, key_id, pending_window_in_days, alias_name_to_delete):
        ''' Delete a key and it's alias from KMS '''
        response = self.kms_client.schedule_key_deletion(
            KeyId=key_id,
            PendingWindowInDays=pending_window_in_days
        )

        if alias_name_to_delete:
            self.kms_client.delete_alias(
                AliasName= "alias/" + alias_name_to_delete
            )

        return response

    def create_kms_key(self, project_name, region_name, policy, create_alias=False):
        ''' Create a KMS key and a alias based on a policy '''
        if policy:
            response = self.kms_client.create_key(
                Policy=policy,
                Tags=[
                    {
                        'TagKey': 'project',
                        'TagValue': project_name
                    },
                ]
            )
        else:
            response = self.kms_client.create_key(
                Tags=[
                    {
                        'TagKey': 'project',
                        'TagValue': project_name
                    },
                ]
            )

        if create_alias:
            alias_key = "alias/%s" % project_name
            self.kms_client.create_alias(
                AliasName=alias_key,
                TargetKeyId=response['KeyMetadata']['KeyId']
            )

        return response
