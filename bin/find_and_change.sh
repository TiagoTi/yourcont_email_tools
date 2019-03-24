#!/usr/bin/env bash
cd templates/email/
pwd
#

if [ "$1" == "dev" ]; then
    echo "GOOD"
    sed -i 's/cid:/..\/..\/static\/email\/img\//g' *
else
    echo "Ok Let's GO"
    sed -i 's/..\/..\/static\/email\/img\//cid:/g' *
fi

#