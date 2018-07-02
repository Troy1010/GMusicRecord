##region Imports
from GMusicRecord import GMRLog
from gmusicapi import Mobileclient
import TM_CommonPy as TM
import datetime
import os
from GMusicRecord import config
##endregion

def DownloadAndCommitRecord():
    GMRLog.debug(TM.FnName()+"`Open")
    ##region Determine library
    print("Retrieving library..")
    api = Mobileclient()
    if not api.login(config["DEFAULT"]["sGMusicUsername"], config["DEFAULT"]["sGMusicPassword"], Mobileclient.FROM_MAC_ADDRESS):
        raise Exception("Google Music login attempt failed under username:"+config["DEFAULT"]["sGMusicUsername"])
    library = api.get_all_songs()
    GMRLog.debug("library:"+TM.Narrator.Narrate(library))
    ##endregion
    ##region Determine cSongTitles
    print("Making and sorting cSongTitles..")
    cSongTitles = []
    for vSong in library:
        cSongTitles.append(vSong['title'])
    cSongTitles.sort()
    GMRLog.debug("cSongTitles:"+TM.Narrator.Narrate(cSongTitles))
    ##endregion
    ##region Make Commit
    print("Writing SongList.txt and making commit..")
    TM.Run("git clone "+config["DEFAULT"]["sRepoURL"])
    os.chdir(TM.GetGitTitleFromURL(config["DEFAULT"]["sRepoURL"]))
    TM.Delete('SongList.txt')
    with open('SongList.txt','w') as vSongListFile:
        for sSongTitle in cSongTitles:
            vSongListFile.write("\n"+sSongTitle)
    TM.Run("git add .")
    TM.Run("git commit -m \""+str(datetime.datetime.now())+"\"")
    TM.Run("git push origin master")
    os.chdir("..")
    ##endregion
    GMRLog.debug(TM.FnName()+"`Close")
