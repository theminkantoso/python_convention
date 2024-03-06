from datetime import datetime


def some_function(some_list: list[int] = [], some_dict: dict[str, int] = {}, date: datetime = datetime.now()):
    print("do not do this!!")
    print("Since python only init these value upon load, means only ONCE, not each time the function is called")
    print("Set default to None")