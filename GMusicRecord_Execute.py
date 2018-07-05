import traceback, sys, os
try:
    ##region Settings
    bWriteLog = True
    sLogFile = os.path.join(__file__,'..','GMR_ExecuteLog.log')
    ##endregion
    ##region LogInit
    import logging
    GMR_ExecuteLog = logging.getLogger(__name__)
    GMR_ExecuteLog.setLevel(logging.DEBUG)
    try:
        os.remove(sLogFile)
    except (PermissionError,FileNotFoundError):
        pass
    if bWriteLog:
        bLogFileIsOpen = False
        try:
            os.rename(sLogFile,sLogFile)
        except PermissionError:
            bLogFileIsOpen = True
        except FileNotFoundError:
            pass
        if not bLogFileIsOpen:
            GMR_ExecuteLog.addHandler(logging.FileHandler(sLogFile))
    ##endregion
    ##region Install GMusicRecord
    import distutils.core
    GMR_ExecuteLog.debug("Installing GMusicRecord")
    distutils.core.run_setup("setup.py",script_args=["install"])
    GMR_ExecuteLog.debug("Finished installing GMusicRecord")
    ##endregion
    ##region Imports
    import GMusicRecord
    import TM_CommonPy as TM
    ##endregion

    GMR_ExecuteLog.debug("Making a record")
    with TM.WorkspaceContext("Workspace",bPostDelete=True):
        GMusicRecord.DownloadAndCommitRecord()
    GMR_ExecuteLog.debug("Done")
except Exception as e:
    print("====================================================================")
    traceback.print_exc()
    os.system('pause')
    sys.exit(1)
