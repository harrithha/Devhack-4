#!/bin/bash
shopt -s expand_aliases
ne=~/.intellish
echo $ne
if [ -d "$ne" ]; then
    echo "Directory $ne exists."
else
    echo "Directory $ne does not exist."
    mkdir -p "$ne"
    cp $(pwd)/{intellish.py,ml_terminal_interface.py} $ne/
fi

if alias your_alias_name >/dev/null 2>&1; then 
    echo "alias exists"
else 
    echo "alias intellish='python $(pwd)/intellish.py'" >> ~/.bashrc
    eval "$(cat ~/.bashrc | tail -n +10)"
    exec bash
    alias intellish='python $(pwd)/intellish.py'
fi
