#!/bin/bash 
echo "Enter the full website that has to be opened"
read website 
echo "Enter the delay time, in seconds, between consecutive openings" 
read time
echo "Enter the delay time,in seconds, for which the site should be kept open" 
read time_open

while true
do
firefox $website &
sleep $time_open
wmctrl -c firefox
sleep $time
done

