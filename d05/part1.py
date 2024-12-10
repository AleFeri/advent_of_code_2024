class Page():
    pre: set[str]
    suc: set[str]

    def __init__(self):
        self.pre = set()
        self.suc = set()

    def __repr__(self):
        return f"{self.pre=}, {self.suc=}"

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
    if not is_valid:
        continue

    result += int(line[len(line)//2])

print(result)
