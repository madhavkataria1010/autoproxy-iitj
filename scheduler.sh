
PYTHON_SCRIPT_PATH="autoproxy.py"
LOG_FILE="logfile.log"

PYTHON_INTERPRETER="/usr/bin/python3"

if [ ! -f "$PYTHON_SCRIPT_PATH" ]; then
  echo "Error: Python script not found at $PYTHON_SCRIPT_PATH"
  exit 1
fi

(
crontab -l 2>/dev/null
echo "0 * * * * $PYTHON_INTERPRETER $PYTHON_SCRIPT_PATH >> $LOG_FILE 2>&1"
echo "@reboot $PYTHON_INTERPRETER $PYTHON_SCRIPT_PATH >> $LOG_FILE 2>&1"
) | crontab -

echo "Cron jobs added:"
crontab -l

