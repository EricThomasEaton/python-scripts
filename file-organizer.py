from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import time

downloads_folder = "/home/eric/Downloads/"
documents_folder = "/home/eric/Documents/unorganized-docs/"
pictures_folder = "/home/eric/Pictures/unorganized/"

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(downloads_folder):
            src = downloads_folder + filename
            pic_location = pictures_folder + filename
            docs_location = documents_folder + filename
            split_file = os.path.splittext(filename)
            file_type = split_file[1]
            if file_type == '.png' or '.jpeg' or '.gif':
                os.rename(src, pic_location)
            elif file_type == '.docx' or '.doc' or '.pdf':
                os.rename(src, docs_location)
            else:
                continue

event_handler = MyHandler()
Observer.schedule(event_handler, downloads_folder, recursive=True)

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    Observer.stop()
Observer.join()
