##region Settings
import os
bWriteLog = True
sLogFile = os.path.join(__file__,'..','GMRLog.log')
##endregion
##region LogInit
import logging
GMRLog = logging.getLogger(__name__)
GMRLog.setLevel(logging.DEBUG)
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
        GMRLog.addHandler(logging.FileHandler(sLogFile))
##endregion
