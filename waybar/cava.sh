#!/bin/bash
bar=" ▂▃▄▅▆▇█"
dict="s/ //g; "
for ((i=0; i<${#bar}; i++)); do
    dict+="s/$i/${bar:i:1}/g; "
done

cava -p ~/.config/cava/config-waybar | while read -r line; do
    echo "{\"text\": \"$(echo "$line" | sed "$dict")\"}"
done
