## Instructions

Set up your CMSSW:
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
#TBD: cmsrel #
cd $_/src
cmsenv 
```

Clone this repository:
```bash
git clone https://github.com/ktht/CustomMCProduction Configuration/CustomCards
scram b -j8
```

Make sure to download the gridpacks yourself!
