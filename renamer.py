import os


def main():
    actual_names_path, new_names_file = get_path_and_file()
    actual_names = get_actual_names(actual_names_path)
    new_names = get_new_names(new_names_file)
    if len(actual_names) == len(new_names):
        rename(actual_names_path, actual_names, new_names)
        quit("Rename was done.")
    else:
        quit("Actual and New names quantities don't match.")


def get_path_and_file():
    print("\nWelcome to File-Renamer\n")
    actual_names_path = input("Select files path: ")
    new_names_file = input("Select name file: ")
    return actual_names_path, new_names_file


def get_actual_names(actual_names_path):
    file_dictionary = dict()
    for file in os.listdir(actual_names_path):
        if "video" in file:
            key = int(file.replace('video','').replace('.mp4',''))
            file_dictionary.update({key:file})  # Example: generated dictionary will have { 1: 'video1.mp4', 10: 'video10.mp4, ... , 2: 'video2.mp4', ... }

    file_list = list()
    for i in range(1,len(file_dictionary)+1):
        file_list.append(file_dictionary[i])  # Example: generated list will have ['video1.mp4','video2.mp4', ... ,'video10.mp4', ... ]

    return file_list


def get_new_names(new_names_file):
    with open(new_names_file) as f:
        names = f.read().splitlines()  # Creates a list with all lines from the NAMES_FILE.
    names = names_sanitization(names)  
    return names


def names_sanitization(names):
    for i in range(len(names)):

        if names[i][-1] == " ":
            names[i] = names[i][:-1]  # This will remove the last withespace if any.

        names[i] = str(i+1) +" - "+ names[i].replace(":",' -').replace("/",'-')  # Windows do not support ':' and '/' in names.

    return names


def rename(actual_names_path, actual_names, new_names):
    for actual_name, new_name in zip(actual_names,new_names):
        #print(f'The file {actual_name} will be renamed to: {new_name+".mp4"}')  # Can be used to check if the final result is the expected one.
        os.rename(actual_names_path+actual_name, actual_names_path+new_name+'.mp4')


if __name__ == '__main__':
    main()

