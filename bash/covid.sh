#!/bin/bash
#this script downloads covid data and displays it
DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHINCREASE=$(echo $DATA | jq '.[0].deathIncrease')
LASTMODIFIED=$(echo $DATA | jq '.[0].lastModified')
HOSPITALIZEDCURRENTLY=$(echo $DATA | jq '.[0]hospitalizedCurrently')

echo "On $TODAY, there were $POSITIVE positive COVID cases"
echo "On $TODAY, there were $NEGATIVE negative COVID cases"
echo "Since $LASTMODIFIED, there was a death count increase by $DEATHINCREASE"
echo "When the system updated on $LASTMODIFIED, there were $HOSPITALIZEDCURRENTLY people in the hospital"

