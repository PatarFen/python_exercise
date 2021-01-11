import os, re

current_working_dir = os.path.abspath(os.getcwd())
pattern = '.py$'

def catch_all_pyFile():
    files = []
    arr = os.listdir('.')

    for _ in arr:
        if re.search(pattern, _) is not None:
            files.append(_)
    return files

def count_file(filename):
    location_path = os.path.join(current_working_dir, filename)
    empty_line = 0
    code_line = 0
    comment_line = 0

    comments_pattern_1 = "^#"
    #comments_pattern_2 = "^"""
    #comments_pattern_3 = "^'''"

    with open(location_path, 'r') as f:
        for line in f:
            #processed_line = list(filter(None, line))
            if line.strip():
                processed_line = list(filter(None, line))
                if '#' in processed_line:
                #if re.search(comments_pattern_1, line):
                    comment_line = comment_line + 1
                else:
                    code_line = code_line + 1
            else:
                empty_line = empty_line + 1
    
    return empty_line, code_line, comment_line
            

if __name__ == "__main__":
    files = catch_all_pyFile()

    for _ in files:
        empty_line, code_line, comment_line = count_file(_)
        print("File name: %s \nempty_line: %d \ncode_line: %d \ncomment_line: %d" %(_, empty_line, code_line, comment_line))
        print("---------------")
    

