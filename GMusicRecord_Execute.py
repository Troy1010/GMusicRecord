try:
    ##region Settings
    bWriteLog = True
    ##endregion
    ##region LogInit
    import logging, os
    sLogFile = os.path.join(__file__,'..','GMR_ExecuteLog.log')
    GMR_ExecuteLog = logging.getLogger(__name__)
    GMR_ExecuteLog.setLevel(logging.DEBUG)
    try:
        os.remove(sLogFile)
    except (PermissionError,FileNotFoundError):
        pass
    if bWriteLog:
        GMR_ExecuteLog.addHandler(logging.FileHandler(sLogFile))
    ##endregion

    GMR_ExecuteLog.debug("Installing GmusicRecord")
    import subprocess
    subprocess.run(['python', 'setup.py', 'install'])

    ##region Imports
    import GMusicRecord
    import TM_CommonPy as TM
    import traceback, sys
    ##endregion


    GMR_ExecuteLog.debug("Making a record")
    TM.MakeDir("Workspace",bCDInto=True)
    GMusicRecord.DownloadAndCommitRecord()
    os.chdir("..")
    TM.Delete("Workspace")
except Exception as e:
    print("====================================================================")
    print("Traceback (most recent call last):")
    traceback.print_tb(e.__traceback__)
    print(e)
    os.system('pause')
    sys.exit(1)
