##region Imports
import TM_CommonPy as TM
import unittest
import os
import GMusicRecord as GMR
from GMusicRecord.tests._Logger import GMRLog_Tests
from GMusicRecord._Config import config
from GMusicRecord.Misc import _MakeCommit
from GMusicRecord.Misc import _WriteSongTitlesTxtFile
##endregion

class Test_GMusicRecord(unittest.TestCase):
    sTestWorkspace = "TestWorkspace/"

    @classmethod
    def setUpClass(self):
        os.chdir(os.path.join('GMusicRecord','tests'))
        TM.Delete(self.sTestWorkspace)

    @classmethod
    def tearDownClass(self):
        os.chdir(os.path.join('..','..'))

    # ------Tests

    #@unittest.skip("Z")
    def test_DownloadAndCommitRecord(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMR.DownloadAndCommitRecord()

    def test_LoadSettings(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMRLog_Tests.debug("config:"+TM.Narrate(list(config['DEFAULT'].values())))

    def test__UnknownChar(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            cSongTitles = ["�����","WhiteLilies","HardcoreRock"]
            _WriteSongTitlesTxtFile(cSongTitles)
            GMRLog_Tests.debug("_WriteSongTitlesTxtFile:"+open("SongList.txt","r").read())
