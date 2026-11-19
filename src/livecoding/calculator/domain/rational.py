# from rational_list import get_numerator, get_denominator, create_rational
from livecoding.calculator.domain.rational_dict import get_numerator, get_denominator, create_rational


# cr_dict(1,2)
# cr_list(3,4)
#
# import rational_dict
# import rational_list
#
# rational_dict.create_rational(1,2)
# rational_list.create_rational(4,5)

def to_str(q) -> str:
    # FIXME Improve the representation (return 2, not 2/1, put the - sign in front of the numerator)
    # return str(get_numerator(q)) + "/" +str(get_denominator(q))
    return f"{get_numerator(q)}/{get_denominator(q)}"


def add_rational(q1, q2):
    # Python functions are first class citizens (they can be used like any variable, assigned, used as
    # parameters etc.)

    gn = get_numerator  # function assignment, not call!
    gd = get_denominator
    # In Python, () is the call operator

    new_numerator = gn(q1) * gd(q2) + gn(q2) * gd(q1)
    new_denominator = gd(q1) * gd(q2)
    return create_rational(new_numerator, new_denominator)


if __name__ == "__main__":
    print("Hello rational!")
    print(create_rational(1, 3))
