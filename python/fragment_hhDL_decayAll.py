import FWCore.ParameterSet.Config as cms

# link to cards:
# https://github.com/cms-sw/genproductions/tree/dac0b0a9a49aeaddc656529d275e5d426effce44/bin/MadGraph5_aMCatNLO/cards/production/13TeV/NonRes_hh/GF_HH_node_SM
# decay fragment from example:
# https://github.com/cms-sw/genproductions/blob/2e8edbb4c940bf3eea6c3f7af51727a6eb545d8a/python/ThirteenTeV/Higgs/HH/ResonanceDecayFilter_example_HHTo2B2L2Nu_madgraph_pythia8_cff.py


externalLHEProducer = cms.EDProducer("ExternalLHEProducer",
    args = cms.vstring('/home/karl/CMSSW_10_6_24/src/GF_HH_node_SM_tarball.tar.xz'),
    nEvents = cms.untracked.uint32(5000),
    numberOfParameters = cms.uint32(1),
    outputFile = cms.string('cmsgrid_final.lhe'),
    scriptName = cms.FileInPath('GeneratorInterface/LHEInterface/data/run_generic_tarball_cvmfs.sh')
)

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *
from Configuration.Generator.Pythia8PowhegEmissionVetoSettings_cfi import *

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
        processParameters = cms.vstring(
            '15:onMode = off',
            '15:onIfAny = 11 13', # only leptonic tau decays
            '23:mMin = 0.05',
            '23:onMode = off',
            '23:onIfAny = 11 12 13 14 15 16', # only leptonic Z decays
            '24:mMin = 0.05',
            '24:onMode = off',
            '24:onIfAny = 11 13 15', # only leptonic W decays
            '25:m0 = 125.0',
            '25:onMode = off',
            '25:onIfMatch = 5 -5',
            '25:onIfMatch = 23 23',
            '25:onIfMatch = 24 -24',
            'ResonanceDecayFilter:filter = on',
            'ResonanceDecayFilter:exclusive = on', #off: require at least the specified number of daughters, on: require exactly the specified number of daughters
            'ResonanceDecayFilter:eMuAsEquivalent = off', #on: treat electrons and muons as equivalent
            'ResonanceDecayFilter:eMuTauAsEquivalent = on', #on: treat electrons, muons , and taus as equivalent
            'ResonanceDecayFilter:allNuAsEquivalent = on', #on: treat all three neutrino flavours as equivalent
            'ResonanceDecayFilter:mothers = 25,23,24', #list of mothers not specified -> count all particles in hard process+resonance decays (better to avoid specifying mothers when including leptons from the lhe in counting, since intermediate resonances are not gauranteed to appear in general
            'ResonanceDecayFilter:daughters = 5,5,11,11,12,12',
          ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters'
                                    )
        )
                         )


ProductionFilterSequence = cms.Sequence(generator)
