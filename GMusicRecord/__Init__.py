##region Settings
bWriteLog = True
##endregion
##region LogInit
import logging, os
sLogFile = os.path.join(__file__,'..','GMRLog.log')
GMRLog = logging.getLogger(__name__)
GMRLog.setLevel(logging.DEBUG)
try:
    os.remove(sLogFile)
except (PermissionError,FileNotFoundError):
    pass
if bWriteLog:
    GMRLog.addHandler(logging.FileHandler(sLogFile))
##endregion
##region configInit
import configparser, sys
import TM_CommonPy as TM
config = configparser.ConfigParser()
sConfigFilePath = os.path.expanduser("~/GMusicRecordSettings.ini")
#---If Settings.txt is absent, write default one
if not os.path.isfile(sConfigFilePath):
    with open(sConfigFilePath,'w') as vFile:
        vFile.write("[DEFAULT]"
            +"\nsGMusicUsername = xxx@gmail.com"
            +"\nsGMusicPassword = xxx"
            +"\nsRepoURL = https://github.com/Troy1010/GMusicRecord1.git"
            )
    TM.MsgBox("Config file not found.\nNew config file generated at:"+sConfigFilePath
        +"\nDefault values are not adequate. Fill out config file and re-run."
        )
    sys.exit(2)
#---Load Settings.txt
config.read(sConfigFilePath)
##endregion

from GMusicRecord.Misc import DownloadAndCommitRecord
