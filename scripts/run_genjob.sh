#!/bin/bash

set -x

echo "Time is: `date`"

IDX=$1
FRAGMENT_NAME=$2
NOF_EVENTS=$3
OUTPUT_DIR=$4

TMP_ID=$SLURM_JOBID
if [ -z "$TMP_ID" ]; then
  TMP_ID=tmp;
fi

PY_CFG=run_$IDX.py
OUT_FILE=tree_$IDX.root

FRAGMENT_PART=Configuration/CustomCards/python/$FRAGMENT_NAME
FRAGMENT_PATH=$CMSSW_BASE/src/$FRAGMENT_PART

if [ ! -f $FRAGMENT_PATH ]; then
  echo "File $FRAGMENT_PATH does not exist";
fi

if [ ! -d $OUTPUT_DIR ]; then
  mkdir -pv $OUTPUT_DIR;
fi

TMP_DIR=/scratch/$USER/$TMP_ID
mkdir -p $TMP_DIR
cd $TMP_DIR

cmsDriver.py $FRAGMENT_PART --fileout file:$OUT_FILE --mc --eventcontent RAWSIM,LHE --datatier GEN,LHE \
  --conditions auto:mc --step LHE,GEN --no_exec --python_filename=$PY_CFG --number=$NOF_EVENTS --nThreads=1 \
  --customise_commands "process.RandomNumberGeneratorService.externalLHEProducer.initialSeed=$IDX; process.RandomNumberGeneratorService.generator.initialSeed=$IDX"

/usr/bin/time --verbose cmsRun $PY_CFG
cp $OUT_FILE $OUTPUT_DIR
sleep 10

cd $CMSSW_BASE/src
rm -rfv $TMP_DIR

echo "Time is: `date`"

set +x

