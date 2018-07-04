##region configInit
import configparser, sys, os
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
            +"\nbDebug = True"
            )
    TM.MsgBox("Config file not found.\nNew config file generated at:"+sConfigFilePath
        +"\nDefault values are not adequate. Fill out config file and re-run."
        )
    sys.exit(2)
#---Load Settings.txt
config.read(sConfigFilePath)
##endregion
