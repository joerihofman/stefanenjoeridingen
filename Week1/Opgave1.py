entity = ['goat', 'wolf', 'cabbage']
path = []
visited = []

# Defines who can eat whom
def eats(x, y):
    if x == 'goat' and y == 'cabbage':
        return True
    elif x == 'wolf' and y == 'goat':
        return True
    else:
        return False

def state_of(who, state):
    try:
        return state[who]
    except KeyError:
        state[who] = False
        return False

def safe_state(state):
    if state_of('man', state) == state_of('goat', state):
        return True
    elif state_of('goat', state) == state_of('wolf', state):
        return False
    elif state_of('goat', state) == state_of('cabbage', state):
        return False
    else:
        return True

def move(who, state):
    if state[who] == 'left':
        state[who] = 'right'
    else:
        state[who] = 'left'
    return state

def goal_reach(state):
    if not state:
        return False
    return (state_of('man', state) == 'right' and
            state_of('goat', state)=='right' and
            state_of('wolf', state)=='right' and
            state_of('cabbage',state)=='right')

# Checks if child is a safe state to move into, and if it is, it adds
# it to the list of states.
def check_add_child(child, list_states):
    if safe_state(child):
        list_states.append(child)
    return list_states

def expand_states(state):
    children = []
    child = state.copy()
    # the man can also move alone
    move('man', child)
    check_add_child(child, children)
    for ent in entity:
        # Move one object on the same side as the man
        if state_of(ent, state) == state_of('man', state):
            child = state.copy()
            move('man', child)
            move(ent, child)
            check_add_child(child, children)
            #else:
        #print "unsafe state", child
    return children


def dfs(node, visited):
    visited.append(node)

    if goal_reach(node):
        return True


    for child in expand_states(node):
        if child not in visited:
            if dfs(child, visited):
                return True

    return False

def find_all_paths(node, path=[]):
    path = path + [node]

    if goal_reach(node):
        return [path]



    paths = []

    for child in expand_states(node):
        if child not in path:
            newpaths = find_all_paths(child, path)

            for newpath in newpaths:
                paths.append(newpath)
    return paths


# Initialization of the global variables
initial_state = {}
initial_state['man'] = 'left'
for e in entity:
    initial_state[e] = 'left'

print(dfs(initial_state, visited))


print("find a path")
for s in visited:
    print(s)


# print(find_all_paths(initial_state))
print("finding all paths")
paths = find_all_paths(initial_state)

for path in paths:
    print("path:")
    for s in path:
        print(s)
