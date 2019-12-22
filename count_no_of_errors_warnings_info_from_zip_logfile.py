"""
the scripts allow us to count no of errors, warnings, info lines in given logfiles zip.
Note- change logfile zip path
athor- Chetan Pawar
"""

import re
import os
import zipfile

class Logs:
    def __init__(self, directory):
        self.directory = directory
        self.no_of_errors = 0
        self.no_of_warnings = 0
        self.no_of_info =0
        self.no_of_error_lines = 0
        
    def process_logfiles(self):
        zip = zipfile.ZipFile(self.directory)
        files = zip.namelist()
        for file in files:
            f = zip.open(file, "r")
            for line in f.readlines():
                if re.findall("\[(.*ERROR.*)\]",str(line))!=[]:
                    self.no_of_errors = self.no_of_errors + 1
                    self.no_of_error_lines = self.no_of_error_lines + 1
                if re.findall("\[(.*WARNING.*)\]",str(line))!=[]:
                    self.no_of_warnings = self.no_of_warnings + 1
                    self.no_of_error_lines = self.no_of_error_lines + 1
                if re.findall("\[(.*INFO.*)\]",str(line))!=[]:
                    self.no_of_info = self.no_of_info + 1
                    self.no_of_error_lines = self.no_of_error_lines + 1
                
            f.close()
        
        return self.no_of_errors, self.no_of_warnings, self.no_of_info, self.no_of_error_lines
     
    def stat(self):
        self.no_of_errors, self.no_of_warnings, self.no_of_info, self.no_of_error_lines = self.process_logfiles()
        print("No of errors:"+str(self.no_of_errors))
        print("No of warnings:"+str(self.no_of_warnings))
        print("No of info:"+str(self.no_of_info))
        print("Total No of error lines:"+str(self.no_of_error_lines))
            
obj = Logs("A:\\logfiles.zip")
obj.stat()
