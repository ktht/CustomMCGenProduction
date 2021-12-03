import FWCore.ParameterSet.Config as cms
import os

externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring(os.path.join(os.environ['CMSSW_BASE'], 'tt0123j_2l_5f_ckm_LO_MLM_tarball.tar.xz')),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

# Link to datacards:
# https://github.com/cms-sw/genproductions/blob/d5884985dba48834c53549976d8a6f2fec66ba17/bin/MadGraph5_aMCatNLO/cards/production/13TeV/tt0123j_2l_5f_ckm_LO_MLM/

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

idx = pythia8CommonSettingsBlock.pythia8CommonSettings.index('ParticleDecays:limitTau0 = on')
pythia8CommonSettingsBlock.pythia8CommonSettings.pop(idx)
pythia8CommonSettingsBlock.pythia8CommonSettings.insert(idx, 'ParticleDecays:limitTau0 = off')

generator = cms.EDFilter("Pythia8HadronizerFilter",
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000.),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        JetMatchingParameters = cms.vstring(
            'JetMatching:setMad = off',
            'JetMatching:scheme = 1',
            'JetMatching:merge = on',
            'JetMatching:jetAlgorithm = 2',
            'JetMatching:etaJetMax = 5.',
            'JetMatching:coneRadius = 1.',
            'JetMatching:slowJetPower = 1',
            'JetMatching:qCut = 70.', #this is the actual merging scale
            'JetMatching:nQmatch = 5', #4 corresponds to 4-flavour scheme (no matching of b-quarks), 5 for 5-flavour scheme
            'JetMatching:nJetMax = 3', #number of partons in born matrix element for highest multiplicity
            'JetMatching:doShowerKt = off', #off for MLM matching, turn on for shower-kT matching
        ),
        processParameters = cms.vstring(
            'TimeShower:mMaxGamma = 1.0',
        ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'JetMatchingParameters',
                                    'processParameters',
                                    )
    )
)
