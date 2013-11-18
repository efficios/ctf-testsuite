#!/bin/sh

for dir in */; do
	echo "Running ${dir} tests"
	cd ${dir}
	./run.sh
	cd ..
done
