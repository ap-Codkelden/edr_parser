#!/usr/bin/env bash

for f in *.xml
do 
echo "Processing $f file.."
# sed -i -e 's/&#([1-9]|[12][0-9]|3[01])//g' -e 's/&#127;\+//g' $f
# sed -i 's/&quot;/\"/g' $f
sed -i -e 's/&#30;\+//g' -e 's/&#3;\+//g' -e 's/&#127;\+//g' -e 's/&#24;\+//g' -e 's/&#14;\+//g' -e 's/&#31;\+//g' $f
done
