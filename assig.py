

""" Program to build a command-line tool that can parse CSV files and perform some basic operations on the data."""

import argparse
import csv

parser = argparse.ArgumentParser(description="A tool for working with CSV files.")
parser.add_argument("filename", nargs="?", help="the name of the CSV file to load")
args = parser.parse_args()

data = []

def load(filename):                                         #Here we Load the csv file in this function
    with open(filename, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)

def count():                                                #function to count length of the data
    print(len(data))

def mean(column):                                           #function to calculate the mean
    values = [float(row[column]) for row in data]
    print(sum(values) / len(values))

def filter(column, value):                                  #function to slice the particular data of choosed column
    global data
    data = [row for row in data if row[column] == value]

if args.filename:
    load(args.filename)

while True:                                                 #Commands to fetch input from the user and call the desired function.
    command = input("> ")
    if command.startswith("load "):
        filename = command.split()[1]
        load(filename)
    elif command == "count":
        count()
    elif command.startswith("mean "):
        column = command.split()[1]
        mean(column)
    elif command.startswith("filter "):
        column, value = command.split()[1:]
        filter(column, value)
    elif command == "exit":
        break
