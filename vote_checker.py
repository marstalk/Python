
voted_dic = {}


def vote_checker(name):
    if voted_dic.get(name):
        print("voted, kick them out")
    else:
        voted_dic[name] = True
        print("let them vote")


vote_checker("mars")
vote_checker("leon")
vote_checker("mars")
vote_checker("lily")
