import random
import maths  # maths had to be imported from the same directory


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        # Indentation was incorrect, the append function was not called inside the for loop.
        # b_list.append(new_item)
        b_list.append(new_item)

    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
