# Logging in Python is handled by using the built-in logging module,
# which allows you to record messages for debuggging, monitoring and error tracking

# Logging Levels
# 1. DEBUG: Gives detailed information for diagnosing problems (Level = 10)
# 2. INFO: Provides general information about the application's execution (Level = 20)
# 3. WARNING: Warns when something unexpected happens, but the application still runs (Level = 30)
# 4. ERROR: When a serious error occured that may cause the program to not function correctly (Level = 40)
# 5. CRITICAL: When a severe error occured that has caused the application to crash (Level = 50)

# When a level is called, it also checks if there are levels above the current level. If there are, then those levels are also displayed.
# However, any levels that are below the current level are not displayed.

import logging

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S", filename="app.log", filemode="w")
# logging.basicConfig(level=logging.INFO)
logging.debug("This is debugging from logging")
logging.info("This is info from logging")
logging.error("This is something from logging")
