
PYTHON_SCRIPT="autoproxy.py"

while true; do
    python3 $PYTHON_SCRIPT

    if [ $? -eq 0 ]; then
        echo "Script working"
        break
    else
        echo "Eait and try again "
    fi
    sleep 2
done
