import boto3
access_key_id='access key'
secret_access_key='secret key'
client = boto3.resource('sqs', region_name= 'ap-south-2',aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
queue_url = 'https://sqs.ap-south-2.amazonaws.com/106885830247/first_queue'


#eue = client.get_queue_by_name(QueueName='first_queue')

#sponse = queue.send_message(MessageBody='Second Hello From Gowrav')

#rint(response)

client = boto3.client('sqs',region_name= 'ap-south-2',aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

QueueUrl = queue_url
response = client.receive_message(
    QueueUrl=QueueUrl,
    AttributeNames=[
        'SentTimestamp'
    ],
    MaxNumberOfMessages=1,
    MessageAttributeNames=[
        'All'
    ],
    VisibilityTimeout=0,
    WaitTimeSeconds=0
)
print(response['Body'])