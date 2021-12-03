#!/bin/bash

IDX=$1
CFG=$2
NOF_EVENTS=$3

source /cvmfs/cms.cern.ch/cmsset_default.sh
cd $HOME/CMSSW_7_1_26
eval $(scramv1 runtime -sh)

run_genjob.sh $IDX fragment_$CFG.py $NOF_EVENTS /hdfs/local/$USER/CustomProduction/$CFG
