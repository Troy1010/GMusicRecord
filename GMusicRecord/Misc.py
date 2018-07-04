##region Imports
from gmusicapi import Mobileclient
import TM_CommonPy as TM
import datetime
import os
from GMusicRecord._Config import config
from GMusicRecord._Logger import GMRLog
##endregion

def _WriteSongTitlesTxtFile(cSongTitles):
    with open('SongList.txt','w',encoding="utf-8") as vSongListFile:
        for sSongTitle in cSongTitles:
            vSongListFile.write("\n"+sSongTitle)

def _MakeCommit(cSongTitles):
    print("Writing SongList.txt and making commit..")
    TM.Run("git clone "+config["DEFAULT"]["sRepoURL"])
    os.chdir(TM.GetGitTitleFromURL(config["DEFAULT"]["sRepoURL"]))
    TM.Delete('SongList.txt')
    _WriteSongTitlesTxtFile(cSongTitles)
    TM.Run("git add .")
    TM.Run("git commit -m \""+str(datetime.datetime.now())+"\"")
    TM.Run("git push origin master")
    os.chdir("..")

def DownloadAndCommitRecord():
    GMRLog.debug(TM.FnName()+"`Open")
    ##region Determine library
    print("Retrieving library..")
    api = Mobileclient()
    if not api.login(config["DEFAULT"]["sGMusicUsername"], config["DEFAULT"]["sGMusicPassword"], Mobileclient.FROM_MAC_ADDRESS):
        raise Exception("Google Music login attempt failed under username:"+config["DEFAULT"]["sGMusicUsername"])
    library = api.get_all_songs()
    GMRLog.debug("library:"+TM.Narrate(library))
    ##endregion
    ##region Determine cSongTitles
    print("Making and sorting cSongTitles..")
    cSongTitles = []
    for vSong in library:
        cSongTitles.append(vSong['title'])
    cSongTitles.sort()
    GMRLog.debug("cSongTitles:"+TM.Narrate(cSongTitles))
    ##endregion
    ##region Make Commit
    _MakeCommit(cSongTitles)
    ##endregion
    GMRLog.debug(TM.FnName()+"`Close")
