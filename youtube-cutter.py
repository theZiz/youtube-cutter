#!/usr/bin/python3
import sys
import subprocess

def do_cutting(start_time,duration,number,title):
	filename = number + ' - ' + title + '.mp3'
	if (len(duration) == 0):
		subprocess.call(["ffmpeg","-v","5","-y","-i",sys.argv[1],"-acodec","libmp3lame","-ac","2","-ab","320k","-ss",start_time,filename])
	else:
		subprocess.call(["ffmpeg","-v","5","-y","-i",sys.argv[1],"-acodec","libmp3lame","-ac","2","-ab","320k","-ss",start_time,"-t",duration,filename])
	tagstring = '%A: Various %t: ' + title + ' %T: ' + number
	subprocess.call(["tagmp3","set",tagstring,filename])

def string_to_seconds(timestamp):
	time_array = timestamp.rsplit(':')
	seconds = int(time_array[0])*60 + int(time_array[1]);
	if (len(time_array) == 3): # with hour
		seconds = seconds * 60 + int(time_array[2])
	return seconds

def seconds_to_string(seconds):
	hours = int(seconds/3600)
	minutes = int(int(seconds/60)%60)
	seconds = int(seconds%60)
	return str(hours).zfill(2) + ':' + str(minutes).zfill(2) + ':' + str(seconds).zfill(2)

if (len(sys.argv) < 3):
	print('Usage: youtube-cutter.py download.m4a description.txt [shift] [end deletion]')

shift = 0
if (len(sys.argv) > 3):
	shift = int(sys.argv[3])

deletion = 0
if (len(sys.argv) > 4):
	deletion = int(sys.argv[4])

start_time = 0
end_time = 0
number = ''
title = ''
lines = [line.rstrip('\n') for line in open(sys.argv[2])]
first_round = True
for line in lines:
	cut_at_first_space = line.split(' ', 1)
	cut_at_second_space = cut_at_first_space[1].split(' ', 1)
	end_time = string_to_seconds(cut_at_second_space[0]) + shift

	# Decoding previous song
	if (not first_round):
		do_cutting(seconds_to_string(start_time),seconds_to_string(end_time-start_time-deletion),number,title)
	first_round = False
	#Loading data of next song
	start_time = end_time;
	number = cut_at_first_space[0]
	if (number[len(number)-1] == '.'):
		number = number[:-1]
	title = cut_at_second_space[1]
do_cutting(seconds_to_string(start_time),'',number,title)
