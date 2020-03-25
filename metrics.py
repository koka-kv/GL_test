#!/usr/bin/env python3
# metrics.py
# Author: Konstiantyn Kanafotskyi (c) 2020

import argparse
import psutil
from collections import namedtuple

def input_parse():
    input_parser = argparse.ArgumentParser(prog='metrics',
                                        description='Print CPU and RAM metrics')
    input_parser.add_argument('Metric', choices=['cpu', 'mem'], type=str, help='Print CPU metrics')

    args = input_parser.parse_args()
    return args.Metric

def metrics_cpu():
    items=['idle', 'user', 'guest', 'iowait', 'stolen', 'system']
    cpu_output = psutil.cpu_times_percent(interval=0.3)

    for item in items:
        get_item=''
        if item == 'stolen':
            get_item = 'steal'
        else:
            get_item = item

        print('{0}.{1} {2}'.format('system.cpu', item, getattr(cpu_output,get_item)))

def metrics_mem():
    items=['total','used','free','shared']
    virtual_mem_output = psutil.virtual_memory()
    
    for item in items:
        print('{0} {1} {2}'.format('virtual',item, getattr(virtual_mem_output,item)))

    swap_mem_output = psutil.swap_memory()
    
    for item in items[:-1]:
        print('{0} {1} {2}'.format('swap', item, getattr(swap_mem_output,item)))

if input_parse() =='cpu':
    metrics_cpu()
else:
    metrics_mem()

