#!/bin/bash
## USAGE:
## bash cacaoify.sh SUBMISSIONSCRIPT ARRAYNUMBER


SubScript=$1
Array=$2

i=1
while [ "$i" -le "$Array" ]; do
    SLURM_ARRAY_TASK_ID=$i nohup bash $SubScript &
    i=$(($i+1))
done
