#!/usr/bin/env python

import dollarpy
from dollarpy import Recognizer, Template, Point
import os
import sys

def print_help():
	print "\n\nUsage: pdollar [-t] [-r] [-i]\n\n Use -t <file-name> to add a template file in the template folder\n Use -r to clear the template folder.\n Use -i <file-name> to take input from an event file.\n\n"

def purge_template_folder():
	file_list = os.listdir('./templates')
	templates_dir_path = os.path.dirname(os.path.realpath(__file__)) + "/templates/"
	for index in range(len(file_list)):
		file_list[index] = templates_dir_path + file_list[index]
		os.remove(file_list[index])
	print "\n\nAll the templates have been successfully removed\n\n"

def start_file_upload(file_path):
	file_arr = file_path.split("/")
	file_name = file_arr[len(file_arr) - 1]
	with open(os.path.dirname(os.path.realpath(__file__)) + "/templates/" + file_name, 'w') as write_file:
		for line in open(file_path):
			write_file.write(line)

def create_template(file_path):
	if os.path.isfile(file_path):
		start_file_upload(file_path)		
	else:
		print "\n\nPlease give a valid file path for adding it to the templates folder"

def add_points_in_list(all_points):
	template_points = []
	for x in range(len(all_points)):
		point = all_points[x].split('/')
		point = point[0]
		if point[0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
			point = point.split(',')
			second_point = point[1].rstrip()
			y = [point[0], second_point]
			template_points.append(y)
	return template_points

def get_eventfile_points(eventfile_path):
	with open(eventfile_path, 'r') as f:
		all_points = f.readlines();
		template_points = []
        	for x in range(len(all_points)):
			point = all_points[x].split('/')
			point = point[0]
			if point[0] in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
				point = point.split(',')
				second_point = point[1].rstrip()
				y = [point[0], second_point]
				template_points.append(y)
	return template_points

def get_points_from_class(template_points):
	a = []
	for i in range(len(template_points)):
		a.append(Point(int(template_points[i][0]), int(template_points[i][1]), 1))
	return a

def find_template(event_file_path):
	templates_list = os.listdir('./templates')
	number_of_templates = len(templates_list)
	all_templates_points = []
	templates_dir_path = os.path.dirname(os.path.realpath(__file__)) + "/templates/"
	for i in range(len(templates_list)):
		with open(templates_dir_path + templates_list[i], 'r') as f:
			all_points = f.readlines();
		all_templates_points.append(add_points_in_list(all_points))
	eventfile_points = get_eventfile_points(event_file_path)
	event_file_points_list = get_points_from_class(eventfile_points)
	for i in range (len(templates_list)):
		present_template_points = get_points_from_class(all_templates_points[i])
		present_template = Template(templates_list[i], present_template_points)
		recognizer = Recognizer([present_template])
		result = recognizer.recognize(event_file_points_list)
		print result
		

def perform_operations(inputs):
	if inputs[1] == '-r':
		purge_template_folder()
	elif inputs[1] == '-t':
		create_template(inputs[2])
	elif inputs[1] == '-i':
		find_template(inputs[2]);

input_length = len(sys.argv)
if input_length == 1:
	print_help()

elif sys.argv[1] not in('-r', '-t', '-i'):
	print_help()
else:
	perform_operations(sys.argv)
