import boto3
import os
import slack
from botocore.exceptions import ClientError

def send_slack(SLACK_TOKEN,SLACK_CHANNEL,MSGBODY):

    client = slack.WebClient(token=SLACK_TOKEN)
    client.chat_postMessage(channel=SLACK_CHANNEL,text=MSGBODY)


def set_desired_capacity(asg_name, desired_capacity):
    print(f"AutoScalingGroup:{asg_name} , Desired Capcity:{desired_capacity}")
    response = client.set_desired_capacity(
        AutoScalingGroupName=asg_name,
        DesiredCapacity=int(desired_capacity),
    )
    return response

def get_asg_info(asg_name):
    response = client.describe_auto_scaling_groups(
    AutoScalingGroupNames=[
        asg_name,
    ]
    )
    return response

def update_asg(asg_name,template_name,template_version,max_size,min_size):
    try:
        response = client.update_auto_scaling_group(
        AutoScalingGroupName = asg_name,
        LaunchTemplate={
            'LaunchTemplateName': template_name ,
            'Version': '{}'.format(template_version),
        },
        MaxSize=int(max_size),
        MinSize=int(min_size),
        # NewInstancesProtectedFromScaleIn=True,
        )
        return response
    except ClientError as e:
        print(f"An error occurred: {e.response['Error']['Message']}")
        return e.response['Error']['Message']
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        return str(e)

if __name__ == '__main__':

    asg_name = os.getenv('ASG_NAME')
    desired_capacity = os.getenv('DESIRED_CAPACITY')
    region = os.getenv('REGION')
    SLACK_TOKEN = os.getenv('SLACK_TOKEN')
    SLACK_CHANNEL = os.getenv('SLACK_CHANNEL')
    print(f"AutoScalingGroup:{asg_name} , Desired Capcity:{desired_capacity}, Region :{region}")
    client = boto3.client('autoscaling',region_name=region)
    template_name = os.getenv("TEMPLATE_NAME")
    template_version = os.getenv("TEMPLATE_VERSION")
    max_size = os.getenv("MAX_NODE")
    min_size = os.getenv("MINI_NODE")
    MSGBODY = update_asg(asg_name,template_name,template_version,max_size,min_size)
    MSGBODY = "AutoScalingGroup:{},Min Node Capcity:{}, Region :{}".format(asg_name,min_size,region) + "\n" + str(MSGBODY)
    print(MSGBODY)
    send_slack(SLACK_TOKEN,SLACK_CHANNEL,MSGBODY)