##region Settings
import os
bWriteLog = True
sLogFile = os.path.join(__file__,'..','GMRLog.log')
##endregion
from GMusicRecord._Config import config
##region LogInit
import logging
GMRLog = logging.getLogger(__name__)
GMRLog.setLevel(logging.DEBUG)
if config["DEFAULT"].getboolean("bDebug"):
    GMRLog.disabled = False
else:
    GMRLog.disabled = True
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
