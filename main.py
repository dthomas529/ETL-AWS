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

    #get object
    response = s3Client.get_object(Bucket=bucket, Key=key)

    #process result for CSV files
    data = response['Body'].read().decode('uft-8') #response is stored in data
    reader = csv.reader(io.StringIO(data)) #data is read by csv reader 
    next(reader) #skips column titles
    for row in reader:
	    print(str.format("Customer ID" - {}, "Referred a Friend - {}, Number of Referrals - {}", row[0], row[1], row[2]))
          
writer = csv.writer(reader)
writer.writerows(data)

print(f"CSV file has been saved successfully.")

