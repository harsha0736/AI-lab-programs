#State representation:(monkey_pop,monkey_status,box_pos,banana_status)
initial_state=('left', 'onfloor', 'middle', 'hasnot')
# Actions
def grasp(state):
    if state == ('middle', 'onbox', 'middle', 'hasnot'):
        return ('middle', 'onbox', 'middle', 'has')
    return None


def climb(state):
    monkey_pos, monkey_status, box_pos, banana_status=state
    if monkey_status == 'onfloor' and monkey_pos == box_pos:
        return (monkey_pos, 'onbox', box_pos, banana_status)
    return None


def push(state, L2):
    monkey_pos, monkey_status, box_pos, banana_status=state
    if monkey_status == 'onfloor' and monkey_pos == box_pos:
        return (L2, 'onfloor', L2, banana_status)
    return None


def walk(state, L2):
    monkey_pos, monkey_status, box_pos, banana_status=state
    if monkey_status == 'onfloor':
        return (L2, 'onfloor', box_pos, banana_status)
    return None


# Goal checking function
def canget(state):
    if state[3] == 'has':  # banana_status == 'has'
        return True, []

    # Define possible actions
    actions=[
        ('grasp', grasp),
        ('climb', climb),
        ('push_middle', lambda s: push(s, 'middle')),
        ('push_left', lambda s: push(s, 'left')),
        ('push_right', lambda s: push(s, 'right')),
        ('walk_middle', lambda s: walk(s, 'middle')),
        ('walk_left', lambda s: walk(s, 'left')),
        ('walk_right', lambda s: walk(s, 'right'))
    ]

    # Try each action
    for action_name, action_fn in actions:
        new_state=action_fn(state)
        if new_state:
            success, plan=canget(new_state)
            if success:
                return True, [action_name] + plan
    return False, []


# Find the solution
success, plan=canget(initial_state)

if success:
    print("Plan to get the banana:", plan)
else:
    print("No plan found.")

