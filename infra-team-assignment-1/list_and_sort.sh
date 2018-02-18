#!/bin/bash

du -hsx * | sort -rh | head -10


filelist=$(find $HOME/Desktop -name '*.*' -type f)
IFS=$'\n'	# To handle spaces in filenames
for i in $filelist
do
	filename=$(echo $i | rev | cut -d'/' -f 1 | rev)
	ext=$(echo $filename | rev | cut -d'.' -f 1 | rev)
	full_path=$HOME/Documents/$ext
	mkdir -p "$full_path"
	mv -i "$i" "$full_path" # Check for overwriting of a file
done
echo "Done"