import json

# chart v3 has a list of asteroids that are in a non-changable order
# each asteroid has a cycle which changes each turn
# an astroid with an offset 0 is an illegal move
# initial offset value is given
# find the shortest path (in terms of turns) to reach the end.


class Ship(object):

    blast_position = 0
    asteroids = []

    potential_nodes = []
    visited_nodes = []
    priority_queue = []

    max_pos = 0

    directions = [1, 0, -1]

    equilibrium = 0

    def __repr__(self):
        return "<Ship at {0} v: {1} t: {2} >".format(self.pos, self.v, self.t)

    def __init__(
        self, asteroids=None, t_per_blast_move=None,
        t=None, p=None, v=None, d=None, parent=None
    ):
        self.asteroids = asteroids
        self.t_per_blast_move = t_per_blast_move
        self.safety_distance = len(self.asteroids)
        self.reverse = False
        self.d = d
        self.t = t
        self.v = v
        self.pos = p
        self.parent = parent

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __eq__(self, other):

        sss = {
            "pos": self.pos, "t": self.t
        }
        other = {
            "pos": other.pos, "t": other.t
        }
        return sss == other

    def __hash__(self):
        return hash((self.v, self.t, self.pos))

    def weight(self):
        return self.pos + self.v + self.t

    def pos_full_next_turn(self, pos):
        ast = self.asteroids[pos - 1]
        if self.reverse:
            ast = self.asteroids[pos]
        cycle = ast.get('t_per_asteroid_cycle')
        if (ast.get('offset') + self.t + 1) % cycle == 0:
            return True
        return False

    def blast_zone_check(self, pos, t):
        if (
            pos <= self.blast_position and
            self.blast_position != 0 and
            pos < 0
        ):
            print('blown to bits at pos: {0} and blast pos :{1}'.format(
                self.pos, self.blast_position))
            return False
        if t > 0 and t % self.t_per_blast_move == 0:
            self.blast_position += self.t_per_blast_move
        return True

    def get_queue(self, visited=[]):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        # position_movement_weight = positions_offset + v + a + d
        out = []
        for dd in self.directions:
            next_pos = self.pos + self.v + dd
            if next_pos < 0:
                continue
            if not self.blast_zone_check(next_pos, self.t):
                continue
            if next_pos >= len(self.asteroids):
                # finishing step
                next_pos = len(self.asteroids) - 1
                return [Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=next_pos, v=self.v + dd, d=dd,
                    t=self.t + 1, parent=self
                )]
            if not self.pos_full_next_turn(next_pos):
                ss = Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=next_pos, v=self.v + dd, d=dd,
                    t=self.t + 1, parent=self
                )
                if ss in self.visited_nodes:
                    continue
                out.append(ss)
        return out

    def get_reverse_queue(self):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        # position_movement_weight = positions_offset + v + a + d
        out = []
        for dd in self.directions:
            next_pos = self.pos - (self.v + dd)
            if next_pos < 0:
                continue
            if not self.blast_zone_check(next_pos, self.t):
                continue
            # if next_pos <= need_to_get_to_position:
            #     print('ASTEROIDS DONEEEEE')
            #     next_pos = len(self.asteroids) - 1
            #     return [next_pos]
            if not self.pos_full_next_turn(next_pos):
                vv = self.v + dd
                pos = self.pos - vv
                ss = Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=pos, v=vv, d=dd,
                    t=self.t + 1, parent=self
                )
                if ss in self.visited_nodes:
                    continue
                out.append(ss)
        return out

    def move(self, reverse=False):
        if reverse:
            self.priority_queue = self.get_reverse_queue()
        else:
            self.priority_queue = self.get_queue()
        while self.priority_queue:
            furthest_child = self.priority_queue.pop(0)
            if furthest_child not in self.visited_nodes:
                self.visited_nodes.append(furthest_child)
                if furthest_child.pos >= len(self.asteroids):
                    # fin
                    break
            if reverse:
                furthest_child.children = furthest_child.get_reverse_queue()
            else:
                furthest_child.children = furthest_child.get_queue()
            for i in furthest_child.children:
                if i not in self.visited_nodes:
                    self.priority_queue.append(i)
                    # add the fastest routes only
                    # if reverse:
                    #     len(self.priority_queue)
                    #     continue
                    # else:
                    break
        return furthest_child


def safe(cycle):
    return cycle != 1


def find_impossible_gaps(asteroids):
    speed = 0
    gap_list = []
    for i in range(0, len(asteroids)):
        ast = asteroids[i]
        cycle = ast.get('t_per_asteroid_cycle')
        # if i == 3725:
        if not safe(cycle) and speed == 0:
            # impossibility start
            # gap_list[i] = speed
            speed += 1
        elif not safe(cycle) and speed != 0:
            # impossibility in progress
            speed += 1
        if safe(cycle) and speed != 0:
            # impossibility end
            start_index = i - (speed + 1)
            gap_list.append((start_index, speed))
            speed = 0
        elif safe(cycle):
            # safe
            speed = 0
    if speed != 0:
        start_index = i - speed
        gap_list.append((start_index, speed))
    return gap_list


with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
start_ship = Ship(
    inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
    t=0, p=0, v=0, parent=None
)
children = start_ship.get_queue()
start_ship.children = children
start_ship.priority_queue += children
ff = start_ship.move()
last_forward_ship = ff
asteroids = ff.asteroids[ff.pos:]


gap_list = find_impossible_gaps(asteroids)
unchangable_ships = []
for index, speed in gap_list:
    pos = ff.pos + index
    vvv = speed + 1
    ddd = 0
    possible_time = 0
    ss = Ship(
        asteroids=ff.asteroids,
        t_per_blast_move=ff.t_per_blast_move,
        p=pos, v=vvv, d=ddd,
        t=possible_time, parent=None
    )
    unchangable_ships.append(ss)

lship = unchangable_ships[-1]
lship.reverse = True
print("SAFETY IS AT : {0}".format(len(ff.asteroids)))
revq = unchangable_ships[-1].get_reverse_queue()

uu = unchangable_ships[0]
uu.reverse = False
children = uu.get_queue()
while not children:
    uu.t += 1
    children = uu.get_queue()
uu.children = children
uu.priority_queue += children

solution_route = uu.move()
print(ff)
while solution_route.parent:
    solution_route = solution_route.parent

# v1 = last_forward_ship.v
# v2 = solution_route.v

# if v1 < v2:
#     v1, v2 = v2, v1

while last_forward_ship.v >= solution_route.v:
    last_forward_ship = last_forward_ship.parent
last_forward_ship = last_forward_ship.parent

last_forward_ship.visited_nodes = []

equilibrium = 0
if equilibrium > 0:
    # direction pref
    prefer = 2
if equilibrium < 0:
    prefer = 0
else:
    prefer = 1


def choose_closest_route_to_equilibrium(ship, queue):
    if ship.equilibrium > 0:
        child = queue[-1]
    elif ship.equilibrium < 0:
        child = queue[0]
    elif ship.equilibrium == 0:
        child = queue[len(queue) // 2]
    return child


def move_with_equilibrium(ship, reverse=False):
    ship.priority_queue = ship.get_queue()
    while ship.priority_queue:
        child = choose_closest_route_to_equilibrium(ship, queue)
        ship.equilibrium += child.d
        queue = child.children = child.get_queue()
    return child



print('-'*90); import pdb; pdb.set_trace()  # breakpoint 34242ce4  noqa  //

print('donezo')

