#!/bin/sh

SOURCE_PATH="$1"
TARGET_PATH="$2"

for f in "$SOURCE_PATH"/*/* ; do
	width=$(magick identify -format "%[fx:w]" $f)
	height=$(magick identify -format "%[fx:h]" $f)

	if [[ $width -gt 1600 && $height -gt 900 ]] ; then
		echo "$f is big enough"
		cp -a "$f" $TARGET_PATH
	fi
done
