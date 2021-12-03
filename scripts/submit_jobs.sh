#!/bin/bash

# submits 4k jobs, each processing 2k events

for cfg in ttbarDL_orig ttbarDL_decayAll hhDL_orig hhDL_decayAll; do
  logdir=/home/karl/CustomProduction/$cfg/logs;
  mkdir -p $logdir;
  for i in `seq 1 1000`; do
    sbatch --partition=main --output=$logdir/out_$i.log \
      $HOME/CMSSW_7_1_26/src/Configuration/CustomCards/scripts/job_wrapper.sh \
      $i fragment_$cfg.py 2000 /hdfs/local/karl/CustomProduction/$cfg;
  done
done
