#!/bin/bash

CERN_USERNAME=$1

if [ -z $CERN_USERNAME ]; then
  echo "Need to provide your CERN username";
  exit 1;
fi

GRIDPACKS=(
  "/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.3.3/GF_HH_node_SM/v1/GF_HH_node_SM_tarball.tar.xz"
  "/cvmfs/cms.cern.ch/phys_generator/gridpacks/slc6_amd64_gcc481/13TeV/madgraph/V5_2.2.2/tt0123j_2l_5f_ckm_LO_MLM/v1/tt0123j_2l_5f_ckm_LO_MLM_tarball.tar.xz"
)

NOF_GRIDPACKS=0
TO_DOWNLOAD=""
for GRIDPACK in ${GRIDPACKS[@]}; do
  if [ ! -f $(basename $GRIDPACK) ]; then
    if [ "$TO_DOWNLOAD" != "" ]; then
      TO_DOWNLOAD+=","
    fi
    TO_DOWNLOAD+=$GRIDPACK;
    NOF_GRIDPACKS+=1;
  fi
done


if [ $NOF_GRIDPACKS -gt 1 ]; then
  TO_DOWNLOAD="{$TO_DOWNLOAD}";
fi

if [ $NOF_GRIDPACKS -gt 0 ]; then
  scp -4 $CERN_USERNAME@lxplus.cern.ch:$TO_DOWNLOAD .;
fi
