def paretentheses_check(filename):
    with open(filename) as rf:
        lines = rf.readlines()
        for line in lines:
            list_check = []
            checked = False
            for letter in line:
                if letter == ')':
                    if len(list_check) != 0:
                        list_check.pop()
                    else:
                        with open("answer.txt", "a") as wf:
                            wf.writelines('incorrect\n')
                        checked = True
                elif letter == '(':
                    list_check.append('(')
            if len(list_check) == 0 and checked == False:
                with open("answer.txt", "a") as wf:
                            wf.writelines('correct\n')
                checked = True
            elif checked == False:
                with open("answer.txt", "a") as wf:
                            wf.writelines('incorrect\n')
                checked = True

filename = input()

paretentheses_check(filename=filename)