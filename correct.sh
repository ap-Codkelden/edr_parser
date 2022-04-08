#!/usr/bin/env bash

for f in *.xml
do 
echo "Processing $f file.."
if [[ "$OSTYPE" == "linux"* ]]; then
	LC_ALL=C sed -i -f sed_comm.txt -e $f
elif [[ "$OSTYPE" == "darwin"* ]]; then
	LC_ALL=C sed -i '' -f sed_comm.txt -r $f
fi
done
