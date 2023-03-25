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
pip install -r requirements.txt
if alias intellish >/dev/null 2>&1; then 
    echo "alias exists"
else 
    echo "alias intellish='python $ne/intellish.py'" >> ~/.bashrc
    exec bash
fi

