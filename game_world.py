world = [[], [], []]  # 0: 배경, 1: 오브젝트, 2: UI

def add_oject(o, depth=1):
    world[depth].append(o)

def add_objects(ol, depth=1):
    world[depth] += ol

def remove_object(o):
    remove_collision_object(o)
    for layer in world:
        if o in layer:
            layer.remove(o)
            return

def update():
    for layer in world:
        for o in layer[:]:
            o.update()

def render():
    for layer in world:
        for o in layer[:]:
            o.draw()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def clear():
    for layer in world:
        layer.clear()
    collsition_pairs.clear()
collsition_pairs = {}
def remove_collision_object(o):
    for pairs in collsition_pairs.values():
        for objects in pairs:
            if o in objects:
                objects.remove(o)

def add_collision_pair(group, a, b):
    if group not in collsition_pairs:
        collsition_pairs[group] = ([], [])
    if a is not None and a not in collsition_pairs[group][0]:
        collsition_pairs[group][0].append(a)
    if b is not None and b not in collsition_pairs[group][1]:
        collsition_pairs[group][1].append(b)
#충돌 페어로 등록된 오브젝트들에 대해 충돌을 검사하고, 충돌 시 콜백 함수를 호출\
def handle_collision():
    for group, pairs in collsition_pairs.items():
        for a in pairs[0][:]:
            for b in pairs[1][:]:
                if a in pairs[0] and b in pairs[1] and collide(a, b):
                    a.handle_collision(group, b)
                    b.handle_collision(group, a)
    
