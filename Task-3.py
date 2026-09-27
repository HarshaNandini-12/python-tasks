import os
import shutil

source = input("Enter source folder: ")
destination = input("Enter destination folder: ")

if not os.path.exists(destination):
    os.mkdir(destination)

for file in os.listdir(source):
    if file.endswith(".jpg"):
        source_file = os.path.join(source, file)
        destination_file = os.path.join(destination, file)
        shutil.move(source_file, destination_file)

print("All JPG files moved successfully!")