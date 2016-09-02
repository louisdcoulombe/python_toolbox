import os
import fnmatch


def find_files(src, pattern='*', ignore_link=False, recursive=False):
    ''' Find all files given a directory. Throws if src does not exists.
        src         : directory to list
        pattern     : return files matching this pattern ( *, ?, [])
        ignore_link : do not return link
        recursive   : search in subfolder
    '''
    file_list = []
    # Find all files
    if recursive:
        for r, d, fl in os.walk(src):
            for f in fl:
                if fnmatch.fnmatch(f, pattern):
                    file_list.append(os.path.join(r, f))

    else:
        file_list = [f for f in os.listdir(src) if fnmatch.fnmatch(f, pattern)]
        file_list = [os.path.join(src, f) for f in file_list]
        file_list = filter(os.path.isfile, file_list)

    # Remove links
    if ignore_link:
        file_list = [f for f in file_list if not os.path.islink(f)]

    return file_list
