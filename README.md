## Instructions

Start singularity:
```bash
singularity exec --home $HOME:/home/$USER --bind /cvmfs --bind /hdfs \
   --bind /home --bind /scratch --pwd /home/$USER --contain --ipc --pid \
  /cvmfs/singularity.opensciencegrid.org/kreczko/workernode:centos6 bash
```

In singularity, set up your CMSSW:
```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cmsrel CMSSW_7_1_26
cd $_/src
cmsenv
```

Clone this repository (unfortunately, git doesn't work in this image):
```bash
rm -rf Configuration/CustomCards
mkdir -p Configuration
wget https://github.com/ktht/CustomMCGenProduction/archive/refs/heads/main.zip
unzip main.zip
mv CustomMCGenProduction-main Configuration/CustomCards
rm main.zip
scram b -j8
```

Make sure to download the gridpacks yourself:
```bash
download_gridpacks.sh YOUR_CERN_USERNAME
```
