#!/usr/bin/env python -B

import argparse

# ./
import whistletips as wt


def list(LoadBalancerName):
    print(wt.instances_to_hostnames(wt.list_lb_instances(LoadBalancerName)))


def add(LoadBalancerName, hostname):
    InstanceId = wt.list_instance_ids(hostname)[0]
    wt.register_instance_with_load_balancer(LoadBalancerName, InstanceId)


def rm(LoadBalancerName, hostname):
    InstanceId = wt.list_instance_ids(hostname)[0]
    wt.deregister_instance_from_load_balancer(LoadBalancerName, InstanceId)


def main():
    parser = argparse.ArgumentParser(description='Manipulate loadbalancers.')
    parser.add_argument('LoadBalancerName')
    action = parser.add_mutually_exclusive_group()
    action.add_argument('--add', help='Add instance to loadbalancer.')
    action.add_argument('--rm', help='Removed instance from loadbalancer.')

    args = parser.parse_args()

    if args.add:
        add(args.LoadBalancerName, args.add)
    elif args.rm:
        rm(args.LoadBalancerName, args.rm)
    else:
        list(args.LoadBalancerName)

if __name__ == '__main__':
    main()
