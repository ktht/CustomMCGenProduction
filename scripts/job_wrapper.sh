#!/bin/bash

# Example (10 events, produces tree_1.root):
# sbatch --partition=short --output=~/some.log job_wrapper.sh 1 ttbarDL_orig 10
#
# For some reason only the full path to the script works

echo "Running on $HOSTNAME"

singularity run --home $HOME:/home/$USER --bind /cvmfs --bind /hdfs \
   --bind /home --bind /scratch --pwd /home/$USER --contain --ipc --pid \
  /cvmfs/singularity.opensciencegrid.org/kreczko/workernode:centos6 $HOME/CMSSW_7_1_26/src/Configuration/CustomCards/scripts/run_job.sh $1 $2 $3
