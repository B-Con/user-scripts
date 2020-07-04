#!/bin/sh

SOURCE_PATH="$1"
OUTPUT_PATH="$2"

PRUNE=''
for f in "$SOURCE_PATH"/* ; do
	width=$(magick identify -format "%[fx:w]" $f)
	height=$(magick identify -format "%[fx:h]" $f)
	ratio=$(bc -l <<< $width/$height)
	
	#echo -n "$(basename $f): "
	#~/bin/resize.py $width $height

	if [[ $width -lt 1600 ]] ; then
		echo "$f not wide enough"
		[ ! -z $PRUNE] && rm "$f"
		continue
	fi

	if [[ $height -lt 900 ]] ; then
		echo "$f not tall enough"
		[ ! -z $PRUNE] && rm "$f"
		continue
	fi
	
	# Allow for up to a pixel of deviation from a perfect 16/9, because some
	# images are off by a fraction of a pixel.
	if (( $(echo $ratio'>'1.776|bc -l) && $(echo $ratio'<'1.7783|bc -l) )) ; then
		true
		#echo "$f is large enough and right ratio"
	else
		echo "$f is large enough but not right ratio: $ratio"
		[ ! -z $PRUNE] && rm "$f"
		#mv "$f" "$OUTPUT_PATH"
	fi
done
