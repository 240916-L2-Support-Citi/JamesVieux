#!/bin/bash



logfile=$(grep -E "FATAL|ERROR" "/var/log/app.log")


while ISF= read -r line; do
    timestamps=$(echo "$line" | grep -oP '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}')
    error_message=$(echo "$line" | grep -oP "\[\w+\]\s+(.*)" | sed 's/^\[\w\+\]\s*//' | sed "s/'/''/g")
    error_level=$(echo "$line" | grep -oP 'ERROR|FATAL')

    DB="logs"    
    user="james"    

    export PGPASSWORD="ashihiro"

    psql -U $user -d $DB -c "INSERT INTO log_entries (timestamps, error_level, error_message) VALUES ('$timestamps', '$error_level', '$error_message')"

done <<< "$logfile"

python3 alert_monitor.py