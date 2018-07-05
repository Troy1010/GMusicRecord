##region Imports
import TM_CommonPy as TM
import unittest
import os
import GMusicRecord as GMR
from GMusicRecord.tests._Logger import GMRLog_Tests
from GMusicRecord._Config import config
from GMusicRecord.Misc import _FormatRecord
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

#    @unittest.skip("Z")
    def test_DownloadAndCommitRecord(self):
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMR.DownloadAndCommitRecord()

    def test_LoadSettings(self):
        GMRLog_Tests.debug("\n\n-------"+TM.FnName())
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            GMRLog_Tests.debug("config:"+TM.Narrate(list(config['DEFAULT'].values())))

    def test_UnknownChar(self):
        GMRLog_Tests.debug("\n\n-------"+TM.FnName())
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            library = [{"title":"�����","artist":"Queen","album":"Innuendo"}
                ,{"title":"WhiteLilies","artist":"Queen","album":"Innuendo"}
                ,{"title":"HardcoreRock","artist":"Queen","album":"Innuendo"}
                ,{"title":u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.',"artist":"Queen","album":"Innuendo"}
                ]
            sRecord = _FormatRecord(library)
            with open('SongList.txt','w',encoding="utf-8") as vSongListFile:
                vSongListFile.write("\n"+sRecord)
            GMRLog_Tests.debug("SongList.txt:"+open("SongList.txt","r",encoding="utf-8").read())

    def test__FormatRecord(self):
        GMRLog_Tests.debug("\n\n-------"+TM.FnName())
        with TM.CopyContext("res/Examples_Backup",self.sTestWorkspace+TM.FnName()):
            library = [{"title":"�����","artist":"Queen","album":"Innuendo"}
                ,{"title":"WhiteLilies","artist":"Queen","album":"Innuendo"}
                ,{"title":"HardcoreRock","artist":"Queen","album":"Innuendo"}
                ,{"title":u'Δ, Й, ק, ‎ م, ๗, あ, 叶, 葉, and 말.',"artist":"Queen","album":"Innuendo"}
                ]
            GMRLog_Tests.debug(_FormatRecord(library))
