#!/usr/bin/env python3

'''
you don't need to run this script,
unless you'd like to update the files here with the latest
version of VSCode.

usage:
1) install and open the latest VSCode
2) press Ctrl-Shift-P or Cmd-Shift-P to open 'quick start'
3) type 'Open Default Keyboard Shortcuts (JSON)' into the box and press Enter
4) copy and paste the resulting json file into
scripts/linux.keybindings.raw.json
scripts/windows.keybindings.raw.json
scripts/macos.keybindings.raw.json
, based on your OS
5) uncomment one of the lines like
processRawFile('linux.keybindings.raw.json')
at the bottom of this file
by removing the # and saving changes.
6) run this script, for example, in a terminal, run
cd scripts
python3 process_json.py
with any recent version of Python.
the script will replace/generate files like
linux.keybindings.json
linux.negative.keybindings.json
in the parent directory.
'''

import re
import os

def makeCommandsNegatives(s):
    # it would be less fragile to actually parse the json,
    # but this should be good enough for now because even if a string
    # like this were to occur in a command, the quotes would be escaped.
    # note: allow any number of spaces after the ".
    sNegative = re.sub(r'(", *")command": "', r'\1command": "-', s)
    if s == sNegative:
        print('Warning: no commands found to make negative.')
    return sNegative

def finishingTouches(filename, osname):
    with open(filename, 'rb') as fIn:
        b = fIn.read()

    # fix line-endings
    if osname == 'windows':
        b = b.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')
    else:
        b = b.replace(b'\r\n', b'\n')

    # for macos, indent everything but the opening [ by 4 spaces
    if osname == 'macos':
        b = b.replace(b'\n', b'\n    ')
        b = b.replace(b'\n    [\n', b'\n[\n')

    # for windows, indent everything but the opening [ by 2 spaces
    if osname == 'windows':
        b = b.replace(b'\r\n', b'\r\n  ')
        b = b.replace(b'\r\n  [\r\n', b'\r\n[\r\n')
    
    # remove unnecessary line
    b = b.replace(b'// Override key bindings by placing them into your key bindings file.', b'')

    with open(filename, 'wb') as fOut:
        fOut.write(b)

def processRawFile(inputFile):
    if not os.path.isfile(inputFile):
        print('Not found: ' + inputFile)
        return

    osname = inputFile.split('.')[0]
    if osname not in ['linux', 'windows', 'macos']:
        print('Expected the filename to start with linux, windows, or macos')
        return

    with open(inputFile, encoding='utf-8') as fIn:
        s = fIn.read()

        # get rid of opening/closing whitespace
        s = s.strip()

        outputFile = '../' + osname + '.keybindings.json'
        with open(outputFile, 'w', encoding='utf-8') as fOut:
            fOut.write(s)

        outputNegFile = '../' + osname + '.negative.keybindings.json'
        with open(outputNegFile, 'w', encoding='utf-8') as fOut:
            fOut.write(makeCommandsNegatives(s))

        finishingTouches(outputFile, osname)
        finishingTouches(outputNegFile, osname)

	# optional manual steps:
	# remove initial comment
	# for negatives, remove suggested commands at the end

if __name__ == '__main__':
    print('Please uncomment a line here and run the script.')
    # print('Processing json')
    # processRawFile('linux.keybindings.raw.json')
    # processRawFile('windows.keybindings.raw.json')
    # processRawFile('macos.keybindings.raw.json')
    # print('Done')


