import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    if suffix is None:
        suffix = ""  # no need to check for suffix return all the files in that case

    if path is None:
        path = "."  # check in the current path

    files = []
    for fileOrDir in os.listdir(path):
        currentPath = os.path.join(path, fileOrDir)
        if os.path.isfile(currentPath) and currentPath.endswith(suffix):
            files.append(currentPath)

        elif os.path.isdir(currentPath):
            files += find_files(suffix, currentPath)

    return files


# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

def check_test_case(suffix, path, expected_output):
    output = find_files(suffix, path)
    if output.sort() == expected_output.sort():
        print("Pass")
    else:
        print("output", output)
        print("Fail")


# Test Case 1
# check if valid arguments are provided then result is correct
check_test_case(".c", "testdir", [
    'testdir/subdir3/subsubdir1/b.c',
    'testdir/t1.c',
    'testdir/subdir5/a.c',
    'testdir/subdir1/a.c'
])

# Test Case 2
# check if suffix is not provided then it should return all the files from all the folders scanning it recursively.
check_test_case(None, "./testdir", [
    './testdir/subdir4/.gitkeep',
    './testdir/subdir3/subsubdir1/b.h',
    './testdir/subdir3/subsubdir1/b.c',
    './testdir/t1.c',
    './testdir/subdir2/.gitkeep',
    './testdir/subdir5/a.h',
    './testdir/subdir5/a.c',
    './testdir/t1.h',
    './testdir/subdir1/a.h',
    './testdir/subdir1/a.c'
])

# Test Case 3
# check if the path is not given then it should check in the current path. This behaviour can be tweak based on the requirements whether we want to throw an error etc.
check_test_case(".xyz", None, [])

# Test Case 4
# check if suffix is not provided and empty directory is pased then it should return []. Note: in our case we have added .gitkeep to keep empty folder for git tracking so we will have .gitkeep filename in output.
check_test_case(None, "./testdir", [
    './testdir/subdir4/.gitkeep',
    './testdir/subdir3/subsubdir1/b.h',
    './testdir/subdir3/subsubdir1/b.c',
    './testdir/t1.c',
    './testdir/subdir2/.gitkeep',
    './testdir/subdir5/a.h',
    './testdir/subdir5/a.c',
    './testdir/t1.h',
    './testdir/subdir1/a.h',
    './testdir/subdir1/a.c'
])
