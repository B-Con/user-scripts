#!/bin/sh

# Use the 1st arg as the target, fallback to a hard-coded guess.
DIR="$1"
[ -z $DIR ] && DIR=/media/tea/images/wallpapers/backdrop
LINK="$HOME/.themes/wallpaper"
LOCK_FILE=/tmp/rotate-wallpaper.lock
trap 'rm -rf "$LOCK_FILE"' EXIT

# If another version is running, just exit (it might be blocked waiting for the
# source).
[[ -f $LOCK_FILE ]] && exit

touch $LOCK_FILE

# Specific to my setup: NFS drive might not yet be mounted, poll for it until
# it is.
while [ ! -d "$DIR" ] ; do
	sleep 5
done

# Pick a random file from the target dir.
FILE=$(ls "$DIR" | sort --random-sort | head -n 1)
FILE_PATH="$DIR/$FILE"

# Update the symlink to point to new image.
ln -sf "$FILE_PATH" "$LINK" || exit 1

# Update the background image.
# Explicitly set DISPLAY so this can be called from cron.
export DISPLAY=:0
feh --bg-fill "$LINK"

# Log what happened.
echo "[$(date)] New wallpaper: $FILE_PATH" >> /tmp/rotate-wallpaper.log
