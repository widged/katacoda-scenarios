#!/bin/bash
clear
wget https://julialang-s3.julialang.org/bin/linux/x64/1.5/julia-1.5.3-linux-x86_64.tar.gz
tar xf julia-1.5.3-linux-x86_64.tar.gz
ln -s ~/julia-1.5.3/bin/julia /usr/local/bin/julia
clear
cd julia || exit
