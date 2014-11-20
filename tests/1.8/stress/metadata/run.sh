#!/bin/sh

for dir in $(find -mindepth 1 -maxdepth 1 -type d | sort); do
	echo "Running ${dir} tests"
	cd ${dir}
	./run.sh
	cd ..
done
