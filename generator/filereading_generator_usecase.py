"""
Here’s a practical use case where a generator is highly efficient: reading and processing large files line-by-line.
This is useful for scenarios where you need to process very large files that can’t fit into memory all at once.

Use Case: Processing a Large Log File

Imagine you have a large log file, access_log.txt, containing millions of lines of server access logs. Each line
contains information like IP address, timestamp, and the requested resource. You need to identify and print lines
that contain a specific IP address, but loading the entire file into memory is impractical.

Solution with a Generator

Using a generator allows you to read and process the file one line at a time, making it memory-efficient.
"""
import os

from dotenv import load_dotenv

load_dotenv()


def find_variable_in_file(file_path, variable):
    with open(file_path, 'r') as file:
        for line in file:
            if variable.strip() in line:
                yield line


file_path = os.getenv("file_path")
variable = os.getenv("variable")

for xcom in find_variable_in_file(file_path, variable):
    print(xcom)
