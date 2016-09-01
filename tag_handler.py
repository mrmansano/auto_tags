#!/usr/bin/python

import sys
from subprocess import call

CTAGS_CMD = '/usr/bin/ctags-exuberant'
CSCOPE_CMD = '/usr/bin/cscope-indexer'

class TagHandler:

    def __init__(self, path):
        self.path = path

    def createTags(self):
        cmd = [CTAGS_CMD, '-R', self.path]
        call(cmd)
        cmd = [CSCOPE_CMD, '-r', self.path]
        call(cmd)

    def updateTags(self, files):
        cmd = [CSCOPE_CMD, '-r', self.path]
        call(cmd)
        cmd = [CTAGS_CMD, '-a']
        for f in files:
            cmd.append('%s' %f)
        call(cmd)
