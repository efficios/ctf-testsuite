#!/bin/bash

TEST_PROG="./test.sh"

for t in $(find -mindepth 1 -maxdepth 1 -type d | sort); do
	if [ -n "${TEST_LIST}" ]; then
		TEST_LIST="${TEST_LIST}\n"
	fi
	TEST_LIST="${TEST_LIST}./test.sh ${t}"
done

echo -e "${TEST_LIST}" | prove --exec '' --merge -
