import logging
import logging.handlers
import os

handler = logging.handlers.WatchedFileHandler(os.environ.get("LOGFILE","second.log"))
format = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(format)
root = logging.getLogger()
root.setLevel(os.environ.get("LOGLEVEL", "INFO"))
root.addHandler(handler)

try:
    exit(main())
except:
    logging.exception("Exception in main()")
    exit(1)