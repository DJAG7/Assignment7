import boto3

#Question 1
# In this assignment, you will gain hands-on experience with AWS Lambda and Boto3, Amazon's SDK for Python. You will create a Lambda function that will automatically manage EC2 instances based on their tags.

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')

    # Auto_Stop the specified instance with ID '021bcaa7b931c68f7'
    auto_stop = 'i-021bcaa7b931c68f7'
    print(f"Instance ID before stripping: {auto_stop}")
    auto_stop = auto_stop.strip()
    print(f"Stopping instance with ID: {auto_stop}")
    ec2.stop_instances(InstanceIds=[auto_stop])
    print(f"Stopped instance: {auto_stop}")

    # Auto_Start the specified instance with ID '0fa1781876816a88e'
    auto_start = 'i-0fa1781876816a88e'
    auto_start = auto_start.strip()
    print(f"Starting instance with ID: {auto_start}")
    ec2.start_instances(InstanceIds=[auto_start])
    print(f"Started instance: {auto_start}")
