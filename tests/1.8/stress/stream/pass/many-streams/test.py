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
	metadata_str = \
	('/* CTF 1.8 */\n'
	'\n'
	'typealias integer {{ size = 8; align = 8; signed = false; base = hex; }} := uint8_t;\n'
	'typealias integer {{ size = 32; align = 8; signed = false; base = hex; }} := uint32_t;\n'
	'typealias integer {{ size = 64; align = 8; signed = false; base = hex; }} := uint64_t;\n'
	'\n'
	'trace {{\n'
	'	major = 1;\n'
	'	minor = 8;\n'
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
	'	}};\n'
	'}};\n').format()

	metadata_f = open(output_metadata, 'w')
	metadata_f.write(metadata_str)
	metadata_f.close()

def generate_stream(stream_nr):
	# Generate stream
	stream_packet_header = [
	  0xC1, 0x1F, 0xFC, 0xC1,	# magic
	  0x2A, 0x64, 0x22, 0xD0, 0x6C, 0xEE, 0x11, 0xE0,
	  0x8C, 0x08, 0xCB, 0x07, 0xD7, 0xB3, 0xA5, 0x64, # uuid
	]
	event_payload = [
	  0x42,
	]
	stream_f = open(output_stream + str(stream_nr), 'wb')
	write_binary(stream_f, stream_packet_header)
	# generate 8-bit per event
	write_binary(stream_f, event_payload)
	stream_f.close()

def generate_streams(array_len):
	for i in range(array_len):
		generate_stream(i)

def test_prepare():
	print('Preparing test for ' + str(array_len) + ' streams')
	os.mkdir(tracedir_name)
	generate_metadata(array_len)
	generate_streams(array_len)

def test_clean():
	print('Cleaning up test for ' + str(array_len) + ' streams')
	try:
		os.remove(output_metadata)
	except:
		pass
	for i in range(array_len):
		try:
			os.remove(output_stream + str(i))
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
