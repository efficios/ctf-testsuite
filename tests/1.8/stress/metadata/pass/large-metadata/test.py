#!/usr/bin/env python3

# Expects either "prepare" or "clean" argument

import sys
import os
import struct

def arg_err():
	print('Please specify "prepare <SIZE>" or "clean <SIZE>" as first argument.')
	sys.exit(-1)

if (len(sys.argv) <= 1):
	arg_err()
mode = sys.argv[1]
if (len(sys.argv) <= 2):
	arg_err()
array_len = int(sys.argv[2])

tracedir_name = './trace-' + str(array_len) + '/'
output_metadata = tracedir_name + 'metadata'
output_stream = tracedir_name + 'stream'


def write_binary(f, arr):
	f.write(bytes(arr))

def generate_metadata(array_len):
	# Generate metadata
	metadata_str1 = \
	('/* CTF 1.8 */\n'
	'\n'
	'typealias integer {{ size = 8; align = 8; signed = false; base = 10; }} := uint8_t;\n'
	'typealias integer {{ size = 32; align = 8; signed = false; base = hex; }} := uint32_t;\n'
	'\n'
	'trace {{\n'
	'	major = 0;\n'
	'	minor = 0;\n'
	'	uuid = "2a6422d0-6cee-11e0-8c08-cb07d7b3a564";\n'
	'	byte_order = le;\n'
	'	packet.header := struct {{\n'
	'		uint32_t magic;\n'
	'		uint8_t uuid[16];\n'
	'	}};\n'
	'}};\n'
	'\n'
	'event {{\n'
	'	name = myevent;\n'
	'	fields := struct {{\n'
	'		uint8_t f;\n'
	'	}};\n').format()

	metadata_char = \
	(' ')

	metadata_str2 = \
	('\n'
	'}};\n'
	'\n').format()

	metadata_f = open(output_metadata, 'w')
	metadata_f.write(metadata_str1)
	for i in range(array_len):
		metadata_f.write(metadata_char.format())
	metadata_f.write(metadata_str2)
	metadata_f.close()

def test_prepare():
	print('Preparing test for large metadata ' + str(array_len) + ' chars')
	os.mkdir(tracedir_name)
	generate_metadata(array_len)

def test_clean():
	print('Cleaning up test for large metadata ' + str(array_len) + ' chars')
	try:
		os.remove(output_metadata)
	except:
		pass
	try:
		os.rmdir(tracedir_name)
	except:
		pass

if (mode == "prepare"):
	test_clean()
	test_prepare()
elif (mode == "clean"):
	test_clean()
else:
	arg_err()
