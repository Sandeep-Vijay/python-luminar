


def vaccination(age):
    if age<=18:
        raise Exception('not eligible for vaccination')
    else:
        print('eligible for vaccination')

vaccination(17)