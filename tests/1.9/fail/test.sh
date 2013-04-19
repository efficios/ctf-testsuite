#!/bin/bash
#
# Copyright (C) - 2013 Christian Babeux <christian.babeux@efficios.com>
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License, version 2 only, as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc., 51
# Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

CURDIR=$(dirname $0)
UTILS_DIR=$CURDIR/../../../utils/

source $UTILS_DIR/tap/tap.sh

NUM_TESTS=1

plan_tests $NUM_TESTS

$CTF_READER_BIN $CTF_READER_OPTS $1 >/dev/null 2>&1

result=$?

is $result 1 $1
