# pip
import boto3

ec2 = boto3.client('ec2')
elb = boto3.client('elb')


def list_instances(filter):
    ec2_instances = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': [filter]
            }
        ]
    )
    instances = []
    for instance in ec2_instances['Reservations']:
        instances += instance['Instances']
    return instances


def list_instance_ids(filter):
    instances = list_instances(filter)
    instanceIds = []
    for instance in instances:
        instanceIds.append(instance['InstanceId'])
    return instanceIds


# Can also be used singularly
def instances_to_hostnames(InstanceIds):
    ec2_instances = ec2.describe_instances(
        InstanceIds=InstanceIds
    )
    instances = []
    for instance in ec2_instances['Reservations']:
        instances += instance['Instances']
    keys = []
    for instance in instances:
        keys.append(instance['Tags'][0])
    hostnames = []
    for key in keys:
        if key['Key'] == 'Name':
            hostnames.append(key['Value'])
    return hostnames


def list_lb_instances(lb_name):
    elb_instances = elb.describe_load_balancers(
        LoadBalancerNames=[lb_name]
    )
    instances = []
    for instance in elb_instances['LoadBalancerDescriptions'][0]['Instances']:
        instances.append(instance['InstanceId'])
    return instances


def register_instance_with_load_balancer(LoadBalancerName, InstanceId):
    elb.register_instances_with_load_balancer(
        LoadBalancerName=LoadBalancerName,
        Instances=[{'InstanceId': InstanceId}]
    )


def deregister_instance_from_load_balancer(LoadBalancerName, InstanceId):
    elb.deregister_instances_from_load_balancer(
        LoadBalancerName=LoadBalancerName,
        Instances=[{'InstanceId': InstanceId}]
    )
