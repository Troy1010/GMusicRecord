##region Settings
import os
bWriteLog = True
sLogFile = os.path.join(__file__,'..','GMRLog_Tests.log')
##endregion
##region LogInit
import logging
GMRLog_Tests = logging.getLogger(__name__)
GMRLog_Tests.setLevel(logging.DEBUG)
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
        GMRLog_Tests.addHandler(logging.FileHandler(sLogFile))
##endregion
