from collections import deque

child_pages = deque()

child_pages.appendleft("A")
child_pages.appendleft("B")
child_pages.appendleft("C")
child_pages.appendleft("D")
child_pages.appendleft("E")

for page in child_pages:
    print(page)
