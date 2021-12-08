#!/bin/bash 
echo "Enter the full website that has to be opened"
read website 
echo "Enter the delay time, in seconds, between consecutive openings" 
read time
echo "Enter the delay time,in seconds, for which the site should be kept open" 
read time_open

while true
do
chrome $website &
sleep $time_open
wmctrl -c chrome
sleep $time
done

