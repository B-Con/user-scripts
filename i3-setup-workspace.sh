#!/bin/sh

if [[ "$#" -ne 1 ]]; then
	echo "Specify the workspance number" >&2
	exit 1
fi

case "$1" in
	''|1)
		i3-msg "workspace 1:bg; append_layout ~/.config/i3/workspace-layout-1.json"

		chromium --app=https://gmail.com
		chromium --app=https://keep.google.com
		chromium --app=https://todoist.com/app
		chromium --app=https://youtube.com/playlist?list=WL
		chromium --app=https://play.google.com/music/listen
		;;
esac

