def simplifyPath(path):
    if path[-1] != "/":
        path += "/"
        
    output_stack = []
    current_word = ""
    last_char = ""
    for char in path:
        if char == "/":
            if last_char == "/":
                last_char = char
                continue
            else:
                if current_word != "":
                    if current_word == ".":
                        current_word = ""
                        continue
                    elif current_word == ".." and len(output_stack) > 2:
                        output_stack.pop()
                        output_stack.pop()
                        current_word = ""
                        continue
                    elif current_word == ".." and len(output_stack) <= 2:
                        current_word = ""
                        continue
        
                    output_stack.append(current_word)
                    current_word = ""
                    
                if len(output_stack) == 0 or (len(output_stack) > 0 and output_stack[-1] != "/"):
                    output_stack.append("/")
                    last_char = char
            
        else:
             current_word += char

        last_char = char


    print(output_stack)
    
    if output_stack[-1] == "/" and len(output_stack) > 1:
        output_stack.pop()

    output = ""
    for token in output_stack:
        output += token

    return output
        
            
    


# Tests
from testsuite import lc_test
lc_test(1, simplifyPath("/home/"), "/home")
lc_test(2, simplifyPath("/home//foo/"), "/home/foo")
lc_test(3, simplifyPath("/home/user/Documents/../Pictures"), "/home/user/Pictures")
lc_test(4, simplifyPath("/../"), "/")
lc_test(5, simplifyPath("/.../a/../b/c/../d/./"), "/.../b/d")
lc_test(6, simplifyPath("/a/../../b/../c//.//"), "/c")
