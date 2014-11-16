#!/usr/bin/env python3

# Expects either "prepare" or "clean" argument

import sys
import os

output_metadata = './metadata'
output_stream = './stream'

def arg_err():
	print('Please specify "prepare" or "clean" as first argument.')
	sys.exit(-1)

if (len(sys.argv) <= 1):
	arg_err()
mode = sys.argv[1]

metadata_str = \
'/* CTF 1.8 */\n' \
'\n' \
'typealias integer { size = 8; align = 8; signed = false; base = 10; } := uint8_t;\n' \
'typealias integer { size = 32; align = 32; signed = false; base = hex; } := uint32_t;\n' \
'\n' \
'trace {\n' \
'	major = 0;\n' \
'	minor = 0;\n' \
'	uuid = "2a6422d0-6cee-11e0-8c08-cb07d7b3a564";\n' \
'	byte_order = le;\n' \
'	packet.header := struct {\n' \
'		uint32_t magic;\n' \
'		uint8_t uuid[16];\n' \
'	};\n' \
'};\n' \
'\n' \
'event {\n' \
'	name = seq;\n' \
'	fields := struct {\n' \
'		uint8_t field[2147483648]; /* 2GB array */\n' \
'	};\n' \
'};\n'

stream_packet_header = [
  0xC1, 0x1F, 0xFC, 0xC1,	# magic
  0x2A, 0x64, 0x22, 0xD0, 0x6C, 0xEE, 0x11, 0xE0,
  0x8C, 0x08, 0xCB, 0x07, 0xD7, 0xB3, 0xA5, 0x64, # uuid
]

array_byte = [ 0x00, ]

def write_binary(f, arr):
	f.write(bytes(arr))

def generate_metadata():
	# Generate metadata
	metadata_f = open(output_metadata, 'w')
	metadata_f.write(metadata_str)
	metadata_f.close()

def generate_stream():
	# Generate stream
	stream_f = open(output_stream, 'wb')
	write_binary(stream_f, stream_packet_header)
	# generate 2GB array as event content
	os.ftruncate(stream_f.fileno(), 2147483648)
	stream_f.close()

def test_prepare():
	print('Preparing test')
	generate_metadata()
	generate_stream()

def test_clean():
	print('Cleaning up test')
	try:
		os.remove(output_metadata)
	except:
		pass
	try:
		os.remove(output_stream)
	except:
		pass

if (mode == "prepare"):
	test_prepare()
elif (mode == "clean"):
	test_clean()
else:
	arg_err()
