##region Settings
bWriteLog = True
##endregion
##region LogInit
import logging, os
sLogFile = os.path.join(__file__,'..','GMRLog.log')
GMRLog = logging.getLogger(__name__)
GMRLog.setLevel(logging.DEBUG)
try:
    os.remove(sLogFile)
except (PermissionError,FileNotFoundError):
    pass
if bWriteLog:
    GMRLog.addHandler(logging.FileHandler(sLogFile))
##endregion

from GMusicRecord.Misc import DownloadAndCommitRecord
