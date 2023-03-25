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

if alias intellish >/dev/null 2>&1; then 
    echo "alias exists"
else 
    echo "alias intellish='python $ne/intellish.py'" >> ~/.bashrc
    exec bash
fi
