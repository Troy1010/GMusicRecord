import traceback, sys, os
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

    import GMusicRecord
    import TM_CommonPy as TM

    GMR_ExecuteLog.debug("Making a record")
    with TM.WorkspaceContext("Workspace",bPostDelete=True):
        GMusicRecord.DownloadAndCommitRecord()
except Exception as e:
    print("====================================================================")
    print("Traceback (most recent call last):")
    traceback.print_tb(e.__traceback__)
    print(e)
    os.system('pause')
    sys.exit(1)
