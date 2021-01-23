def group_word_check(
        string: str) -> bool:
    if len(string) == len(set(string)):
        return True
    else:
        for i in range(len(string)):
            if string[i] == string[i - 1]:
                return True
    return False


print(group_word_check('aba'))
