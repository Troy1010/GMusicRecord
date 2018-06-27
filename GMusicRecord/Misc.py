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
    api = Mobileclient()
    api.login(config.sGMusicUsername, config.sGMusicPassword, Mobileclient.FROM_MAC_ADDRESS)
    library = api.get_all_songs()
    GMRLog.debug("library:"+TM.Narrator.Narrate(library))
    ##endregion
    ##region Determine cSongTitles
    cSongTitles = []
    for vSong in library:
        cSongTitles.append(vSong['title'])
    cSongTitles.sort()
    GMRLog.debug("cSongTitles:"+TM.Narrator.Narrate(cSongTitles))
    ##endregion
    ##region Make Commit
    TM.Run("git clone "+config.sRepoURL)
    os.chdir(config.sRepoTitle)
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
