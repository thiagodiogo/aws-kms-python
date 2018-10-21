# aws-kms-rds-crypto-shred

Simple example python code to use AWS Key Management Service (KMS) to create a Master Key and create a RDS Database encrypting it with this MK.

The deletion of the database is via RDS API and the shred is based on the Crypto-Shredding (https://en.wikipedia.org/wiki/Crypto-shredding) concept.

When deleting the database, the option `SkipFinalSnapshot` is setted to `True` to not generate a final snapshot. Also, all automated backups (snapshots) are deleted and can't be recovered (https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DeleteInstance.html).

In order to comply with NIST 800-53, all KMS API calls are logged in AWS CloudWatch, being a proof of the key deletion.

## Installation

Configure AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html

Install boto3:
`pip install boto3`

## Usage

Create KMS Key and DB:
`python create_key_and_db.py`

Delete DB and delete KMS Key (shred):
`python delete_db_and_shred.py`
