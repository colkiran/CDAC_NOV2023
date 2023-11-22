
class TooYoung(Exception):
    pass

class TooOld(Exception):
    pass

class Young(Exception):
    pass


age = 23
try:
    if age <= 6:
        raise TooYoung
    elif age < 18:
        raise Young
    elif age > 100:
        raise TooOld
    else:
        print("You can cast your valueable vote....")
except TooYoung:
    print("Person is too tiny to cast a vote....")
except Young:
    print("Person is young to cast the vote.....")
except TooOld:
    print("Person is too old to cast the vote.....")
