#!/bin/bash

# submit_jobs.sh 1 1000 2000
# submits 4x1000=4000 jobs, each processing 2k events

IDX1=$1
IDX2=$2
NOF_EVENTS=$3

if [ "$IDX1" -gt "$IDX1" ]; then
  echo "Invalid parameters: $IDX1, $IDX2"
  exit 1;
fi

for cfg in ttbarDL_orig ttbarDL_decayAll hhDL_orig hhDL_decayAll; do
  logdir=/home/karl/CustomProduction/$cfg/logs;
  mkdir -pv $logdir;
  for i in `seq $IDX1 $IDX2`; do
    sbatch --partition=main --output=$logdir/out_$i.log \
      $HOME/CMSSW_7_1_26/src/Configuration/CustomCards/scripts/job_wrapper.sh \
      $i $cfg $NOF_EVENTS /hdfs/local/karl/CustomProduction/$cfg;
  done
done
