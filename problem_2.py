import os


def find_files(suffix, path):
    if not os.path.isdir(path):
        print("Add a valid directory path")
        return []

    if not suffix or len(suffix) == 0 or suffix.isnumeric():
        print("This is not a valid suffix", str(suffix))
        return []

    files_found = []
    for f in os.listdir(path):
        if os.path.isfile(path + f):
            if f.endswith(suffix):
                files_found.append(path + f)
        else:
            files_found += find_files(suffix, path + f + '/')
    return files_found


if __name__ == '__main__':
    path = ' C:/Users/PC/Downloads/'
    print(find_files('.c',path +'testdir/'))  # return all files with .c extension in testdir/
    print(find_files('.h',path + 'testdir/'))  # return all files with .h extension in testdir/
    print(find_files('.h', path + 'te'))  # te is not a valid dir
    print(find_files('',path + 'testdir/'))  # '' suffix is not valid
