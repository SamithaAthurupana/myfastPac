from typing import Optional


def get_full_name(first_name:str, last_name:str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def get_name_with_age(name:str , age:int):
    name_with_age = name + "is now: " + str(age)
    return name_with_age
#Now you know that you have to fix it, convert age to a string with str(age):

def process_items(items_t: tuple[int,int,str], items_s: set[bytes]):
    return items_t, items_s
#This means:
    #The variable items_t is a tuple with 3 items, an int, another int, and a str.
    #The variable items_s is a set, and each of its items is of type bytes.

def dic_process_items(prices: dict[str,float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)
#This means:
#The variable prices is a dict:
#The keys of this dict are of type str (let's say, the name of each item).
#The values of this dict are of type float (let's say, the price of each item).

def process_item_or(item: int | str):
    print(item)

def say_hi(name: Optional[str] =None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello world")
# Using Optional[str] instead of just str will let the editor help you detect errors where you
# could be assuming that a value is always a str, when it could actually be None too.

def say_hi_3_10(name:str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello world")


if __name__ == '__main__':
    print(get_full_name("samitha","athurupana"))
    print(get_name_with_age("Samitha",27))
    print(process_items((3,4,"s"),[343]))
    dic_process_items({"Book": 0.3})
    process_item_or(89)
    say_hi()
    say_hi_3_10()
