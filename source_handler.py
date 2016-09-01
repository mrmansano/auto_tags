#!/usr/bin/python

import time
from tag_handler import TagHandler
from watchdog.events import RegexMatchingEventHandler

class SourceFileEventHandler(RegexMatchingEventHandler):
    def __init__(self, path):
        super(SourceFileEventHandler, self).__init__(regexes=[r".*\.c", r".*\.cpp", r".*\.h"])
        self.tag_handler = TagHandler(path)
        self.tag_handler.createTags()

    def update_tag_file(self, file):
        mod_file_list = []
        mod_file_list.append(file)
        self.tag_handler.updateTags(mod_file_list)

    def on_modified(self, event):
        self.update_tag_file(event.src_path)

    def on_created(self, event):
        self.update_tag_file(event.src_path)

    def on_deleted(self, event):
        self.tag_handler.createTags()
