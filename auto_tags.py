#!/usr/bin/python

import sys
import time
from watchdog.observers import Observer
from source_handler import SourceFileEventHandler

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = SourceFileEventHandler(path)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
