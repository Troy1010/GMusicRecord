##region Imports
import TM_CommonPy as TM
import unittest
import os
import GMusicRecord as GMR
from GMusicRecord import GMRLog
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

    @unittest.skip("z")
    def test_DownloadAndCommitRecord(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMR.DownloadAndCommitRecord()

    def test_LoadSettings(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMRLog.debug("config:"+TM.Narrator.Narrate(GMR.config["DEFAULT"].items()))
