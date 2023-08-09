current_branch_stack = []
class_name_map = []
depth_map = []
current_depth = 0

file = open("graph_maker\something.txt", "r")
contents = file.read()
lines = contents.split("\n")
for line in lines:
    depth_map.append(line.count(" ") // 2)
    class_name_map.append(line.strip())

def remove():
    global depth_map
    global class_name_map
    depth_map.pop(0)
    class_name_map.pop(0)

def get_next_depth():
    return depth_map[0]

def make_transition():
    print(current_branch_stack[len(current_branch_stack) - 2] + " -> " + current_branch_stack[len(current_branch_stack) - 1])

def pop():
    current_branch_stack.pop(len(current_branch_stack) - 1)

def push():
    current_branch_stack.append(class_name_map[0])

push()
remove()
while len(class_name_map) > 0:
    if (get_next_depth() == current_depth):
        pop()
        push()
    elif (get_next_depth() == current_depth + 1):
        push()
        current_depth += 1
    elif (get_next_depth() < current_depth):
        next = get_next_depth()
        while next != current_depth:
            pop()
            current_depth -= 1
        pop()
        push()
    make_transition()
    remove()

