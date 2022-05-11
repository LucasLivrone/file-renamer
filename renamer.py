
import os


PATH = 'path-to-files/'
NAMES_FILE = 'file-with-names'


def main():
    actual_names = get_actual_names()
    new_names = get_new_names()
    if len(actual_names) == len(new_names):
        rename(actual_names, new_names)
        quit("Rename was done.")
    else:
        quit("Actual and New names quantities don't match.")


def get_actual_names():
    file_dictionary = dict()
    for file in os.listdir(PATH):
        if "lesson" in file:
            key = int(file.replace('lesson','').replace('.mp4',''))
            file_dictionary.update({key:file})  # Generated dictionary will have { 1: 'video1.mp4', 10: 'video10.mp4, ... , 2: 'video2.mp4', ... }

    file_list = list()
    for i in range(1,len(file_dictionary)+1):
        file_list.append(file_dictionary[i])  # Generated list will have ['video1.mp4','video2.mp4', ... ,'video10.mp4', ... ]

    return file_list


def get_new_names():
    with open(PATH+NAMES_FILE) as f:
        names = f.read().splitlines()  # Creates a list with all lines from the NAMES_FILE.
    names = names_sanitization(names)  
    return names


def names_sanitization(names):
    for i in range(len(names)):

        if names[i][-1] == " ":
            names[i] = names[i][:-1]  # This will remove the last withespace if any.

        names[i] = str(i+1) +" - "+ names[i].replace(":",' -').replace("/",'-')  # Windows do not support ':' and '/' in names.

    return names


def rename(files, names):
    for file, name in zip(files,names):
        #print(f'The file {file} will be renamed to: {name+".mp4"}')  # Can be used to check if the final result is the expected one.
        os.rename(PATH+file,PATH+name+'.mp4')


if __name__ == '__main__':
    main()

