#!/bin/bash
ne=~/.intellish
echo $ne
if [ -d "$ne" ]; then
    echo "Directory $ne exists."
else
    echo "Directory $ne does not exist."
    mkdir -p "$ne"
    cp *.py $ne
fi
ALIAS="intellish"

if grep -q "^alias $ALIAS=" ~/.bashrc; then 
    echo "alias already exists"
else 
    echo "alias intellish='python $ne/intellish.py'" >> ~/.bashrc
    exec bash
fi

