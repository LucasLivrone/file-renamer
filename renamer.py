import os


def main():
    actual_names_path, new_names_file, name_pattern, file_extension = get_path_and_file()
    actual_names = get_actual_names(actual_names_path, name_pattern, file_extension)
    new_names = get_new_names(new_names_file)
    if len(actual_names) == len(new_names):
        rename(actual_names_path, actual_names, new_names, file_extension)
    else:
        quit("Actual and New names quantities don't match.")


def get_path_and_file():
    print("\nWelcome to File-Renamer\n")
    actual_names_path = input("Select files path: ")
    new_names_file = input("Select name file: ")
    name_pattern = input("Select name pattern: ")
    file_extension = input("Select file extension: ")
    return actual_names_path, new_names_file, name_pattern, file_extension


def get_actual_names(actual_names_path, name_pattern, file_extension):
    file_dictionary = dict()
    for file in os.listdir(actual_names_path):
        if name_pattern in file:
            key = int(file.replace(name_pattern,'').replace(file_extension,''))
            file_dictionary.update({key:file})  # Example: generated dictionary will have { 1: 'video1.mp4', 10: 'video10.mp4, ... , 2: 'video2.mp4', ... }

    file_list = list()
    for i in range(1,len(file_dictionary)+1):
        file_list.append(file_dictionary[i])  # Example: generated list will have ['video1.mp4','video2.mp4', ... ,'video10.mp4', ... ]

    return file_list


def get_new_names(new_names_file):
    with open(new_names_file) as f:
        names = f.read().splitlines()  # Creates a list with all lines from new_names_file.
    names = names_sanitization(names)  
    return names


def names_sanitization(names):
    for i in range(len(names)):

        if names[i][-1] == " ":
            names[i] = names[i][:-1]  # This will remove the last withespace if any.

        names[i] = str(i+1) +" - "+ names[i].replace(":",' -').replace("/",'-')  # Windows do not support ':' and '/' in names.

    return names


def rename(actual_names_path, actual_names, new_names, file_extension):
    preview = input("\nType 'yes' to see a preview of final result: ")
    if preview == 'yes':
        for actual_name, new_name in zip(actual_names,new_names):
            print(f'The file {actual_name} will be renamed to: {new_name+file_extension}')

    confirmation = input("\nType 'yes' to confirm rename: ")
    if confirmation == 'yes':
        for actual_name, new_name in zip(actual_names,new_names):
            os.rename(actual_names_path+actual_name, actual_names_path+new_name+'.mp4')
        quit("\nRename was done.")
    else:
        quit("\nRename was cancelled.")


if __name__ == '__main__':
    main()

