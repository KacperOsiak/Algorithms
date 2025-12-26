def is_isogram(string):
    string = string.lower()
    seen_letters = []

    for s in string:
        if s in seen_letters:
            return False
        seen_letters.append(s)
    return True
