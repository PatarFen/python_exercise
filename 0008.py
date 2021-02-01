import os, re

current_working_dir = os.path.abspath(os.getcwd())
pattern1 = r"<[0-9A-Za-z]+>"
pattern2 = r"</[0-9A-Za-z]+>"

def find_body_content(file:str):
    file_location = os.path.join(current_working_dir, file)
    content = []
    find_target = False

    with open(file_location, 'r') as f:
        for line in f:
            if find_target:
                if "</body>" in line:
                    find_target = False
                    pass
                else:
                    line = remove_tag(line)
                    content.append(line)
            else:
                if "<body>" in line:
                    find_target = True
                else:
                    pass
    f.close()

    return content
            
def remove_tag(text:str):
    while re.search(pattern1, text) or re.search(pattern2, text):
        left = re.search(pattern1, text)
        if left and left.span()[1] < len(text):
            text = text[left.span()[1]:]
            right = re.search(pattern2, text)
            if right and len(text) > right.span()[1] - right.span()[0]:
               text = text[:right.span()[0]]
               print(text)
            else:
                break
        else:
            break
    return text
            


test = find_body_content("test.html")
print(test)

