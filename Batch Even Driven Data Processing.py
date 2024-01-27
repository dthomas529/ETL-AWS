import json
import boto3 #callback into S#
import csv
import io #handles input/output as response is read

s3Client = boto3.client('s3')

def lambda_handler(event, context): #contains meta data for the file in the bucket
    #get S3 bucket name from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['bucket']['key']

    print(bucket)
    print(key)
