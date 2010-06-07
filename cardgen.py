#!/usr/bin/env python
from Cheetah.Template import Template
import re, sys, optparse

template = 'template.tex'
re_text = r'^(.+):$\n((?:\n?.+)+)\n*'
rec = re.compile(re_text, re.MULTILINE)

# Eat stderr
class Discarder(object):
    def write(self, text):
        pass

def getMatches(file):
    text = file.read()
    matches = rec.finditer(text)
    return matches

def main():
    p = optparse.OptionParser()
    p.add_option('-i', '--input', help='Card definition file')
    p.add_option('-o', '--output', help='Output File')
    options, args = p.parse_args()
    
    infile = sys.stdin
    outfile = sys.stdout
    
    if options.input is not None:
        infile = open(str(options.input), 'r')
        
    if options.output is not None:
        outfile = open(str(options.output), 'w')
    
    cards = getMatches(infile)
    
    # get rid of cheetah stderr output
    temp = sys.stderr
    sys.stderr = Discarder()
    outfile.write(str(Template(file=template, searchList = { 'cards': cards })))
    # restore stderr
    sys.stderr = temp
    
    if options.input is not None:
        infile.close()
    if options.output is not None:
        outfile.close()
    
if __name__ == '__main__':
    main()