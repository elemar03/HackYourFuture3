

def card_validate(number):
    if type(number) != int:
        raise Exception("This is not a number")
    if len(number) != 16:
        raise Exception("Length incorrect")
    number



card_validate(54673)