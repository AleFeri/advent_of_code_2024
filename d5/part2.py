from functools import cmp_to_key

class Page():
    pre: set[str]
    suc: set[str]

    def __init__(self):
        self.pre = set()
        self.suc = set()

    def __repr__(self):
        return f"{self.pre=}, {self.suc=}"

def num_is_lower(page_order_list: dict[str, Page], num: str, other_num: str):
    return other_num in page_order_list[num].pre

with open('input.txt') as input_file:
    starting_text = input_file.read()

starting_text_order_section, starting_text_lists = starting_text.split("\n\n")

page_order_list: dict[str, Page] = {}
for line in starting_text_order_section.split("\n"):
    pre, suc = line.strip("\n").split("|")
    if not page_order_list.get(pre):
        page_order_list[pre] = Page()
    if not page_order_list.get(suc):
        page_order_list[suc] = Page()
    page_order_list[pre].suc.add(suc)
    page_order_list[suc].pre.add(pre)

result = 0
for line in starting_text_lists.split("\n"):
    line = line.strip("\n").split(",")
    is_valid = True
    for i, num in enumerate(line):
        if (
            num == '' or
            page_order_list[num].pre & set(line[i+1:]) or
            page_order_list[num].suc & set(line[:i])
        ):
            is_valid = False
            break
    if is_valid:
        continue

    reordered_list = line.copy()
    reordered_list.sort(key=cmp_to_key(lambda item1, item2: -1 if num_is_lower(page_order_list, item1, item2) else 1))

    result += int(reordered_list[len(reordered_list)//2] or 0)

print(result)
