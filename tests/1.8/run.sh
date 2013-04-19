#!/bin/sh

echo "Running expected pass tests"
cd pass
./run.sh
cd ..

echo "Running expected failure tests"
cd fail
./run.sh
cd ,,
