#!/bin/sh

DIR=/media/tea/images/wallpapers/backdrop
[[ ! -d "$DIR" ]] && i3lock
i3lock -c 181b22 -i $(ls "$DIR"/*.png | sort --random-sort | head -n 1)

