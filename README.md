# autoproxy-iitj

This project is designed to automate the proxy login process for IITJ using a Python script.

## Overview

The project consists of a Python script (`autoproxy.py`) that automates the login process to the IITJ proxy. A scheduler script (`scheduler.sh`) is included to run the Python script at regular intervals (every 2 seconds) until it completes successfully.

## Usage

### Running the Python Script

To manually run the Python script:

```bash
python3 autoproxy.py
```

### Running the Scheduler

To automate the process and run the Python script every 2 seconds until it completes:

1. Make the `scheduler.sh` script executable:

   ```bash
   chmod +x scheduler.sh
   ```

2. Run the `scheduler.sh` script:

   ```bash
   ./scheduler.sh
   ```

The `scheduler.sh` script will continue to run `autoproxy.py` every 2 seconds until the Python script completes successfully. Once the script completes, the scheduler will exit.

## Files

- **autoproxy.py**: The Python script that handles the proxy login.
- **scheduler.sh**: The shell script that runs `autoproxy.py` every 2 seconds until it completes successfully.

## Requirements

- Python 3.x
- lynx (browser installed)
- Bash shell (for running `scheduler.sh`)


