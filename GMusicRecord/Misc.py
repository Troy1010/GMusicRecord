##region Imports
from gmusicapi import Mobileclient
import TM_CommonPy as TM
import datetime
import os
from GMusicRecord._Config import config
from GMusicRecord._Logger import GMRLog
##endregion
def _FormatRecord(library):
    print("Formatting Record..")
    cRecord = []
    for vSong in library:
        cRecord.append(vSong['title'])
    cRecord.sort()
    GMRLog.debug("cRecord:"+TM.Narrate(cRecord))
    return "\n".join(cRecord)

def _MakeCommit(sRecord):
    print("Writing SongList.txt and making commit..")
    TM.Run("git clone "+config["DEFAULT"]["sRepoURL"])
    os.chdir(TM.GetGitTitleFromURL(config["DEFAULT"]["sRepoURL"]))
    TM.Delete('SongList.txt')
    with open('SongList.txt','w',encoding="utf-8") as vSongListFile:
        vSongListFile.write("\n"+sRecord)
    TM.Run("git add .")
    TM.Run("git commit -m \""+str(datetime.datetime.now())+"\"")
    TM.Run("git push origin master")
    os.chdir("..")

def _GetLibrary():
    print("Retrieving library..")
    api = Mobileclient()
    if not api.login(config["DEFAULT"]["sGMusicUsername"], config["DEFAULT"]["sGMusicPassword"], Mobileclient.FROM_MAC_ADDRESS):
        raise Exception("Google Music login attempt failed under username:"+config["DEFAULT"]["sGMusicUsername"])
    library = api.get_all_songs()
    GMRLog.debug("library:"+TM.Narrate(library))
    return library


def DownloadAndCommitRecord():
    GMRLog.debug(TM.FnName()+"`Open")
    ##region Determine library
    library = _GetLibrary()
    ##endregion
    ##region Determine sRecord
    sRecord = _FormatRecord(library)
    ##endregion
    ##region Make Commit
    _MakeCommit(sRecord)
    ##endregion
    GMRLog.debug(TM.FnName()+"`Close")
