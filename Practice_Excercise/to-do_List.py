do_list = []

def add_to_list(item):
    do_list.append(item)
    return do_list

def remove_from_list(item):
    if item in do_list:
        do_list.remove(item)
    return do_list

def list_to_do_list():
    for i in do_list:
        print(i)


add_to_list("clean bathroom")
add_to_list("clean dishes")
add_to_list("make the bed")

print("This is your to do list")
list_to_do_list()

