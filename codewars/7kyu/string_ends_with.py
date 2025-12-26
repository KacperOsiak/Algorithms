def solution(text, ending):
    if ending == "":
        return True
    return text[-len(ending):] == ending