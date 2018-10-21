#!/usr/bin/python
from __future__ import print_function
import boto3

class RdsHelper:
    """RdsHelper class"""

    def __init__(self, region_name):
        self.rds_client = boto3.client('rds', region_name=region_name)

    def create_postgres_database(self, project_name, db_instance_class, az_name, retention_period, kms_key, master_username, master_password):
        ''' Create a PostgreSQL database in RDS using a KMS key encryption '''
        rds_response = self.rds_client.create_db_instance(
            DBName=project_name,
            DBInstanceIdentifier=project_name,
            AllocatedStorage=20,
            DBInstanceClass=db_instance_class,
            Engine='postgres',
            MasterUsername=master_username,
            MasterUserPassword=master_password,
            # DBSecurityGroups=[
            #     'DBSecurityGroups',
            # ],
            # VpcSecurityGroupIds=[
            #     'string',
            # ],
            AvailabilityZone=az_name,
            # DBSubnetGroupName='DBSubnet',
            BackupRetentionPeriod=retention_period,
            Port=5432,
            MultiAZ=False,
            EngineVersion='10.5',
            AutoMinorVersionUpgrade=True,
            LicenseModel='postgresql-license',
            PubliclyAccessible=False,
            Tags=[
                {
                    'Key': 'project',
                    'Value': project_name
                },
            ],
            StorageType='gp2',
            StorageEncrypted=True,
            KmsKeyId=kms_key['KeyMetadata']['KeyId']
        )
        return rds_response

    def delete_database(self, project_name):
        ''' Delete a database in RDS '''
        rds_response = self.rds_client.delete_db_instance(
            DBInstanceIdentifier=project_name,
            SkipFinalSnapshot=True
        )
        return rds_response
