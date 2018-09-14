import json

# chart v3 has a list of asteroids that are in a non-changable order
# each asteroid has a cycle which changes each turn
# an astroid with an offset 0 is an illegal move
# initial offset value is given
# find the shortest path (in terms of turns) to reach the end.


with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)


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
        self.reverse = False
        self.asteroids = asteroids
        self.t_per_blast_move = t_per_blast_move
        self.safety_distance = len(self.asteroids)
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

    def move(self):
        self.priority_queue = self.get_queue()
        while self.priority_queue:
            furthest_child = self.priority_queue.pop(0)
            if furthest_child not in self.visited_nodes:
                self.visited_nodes.append(furthest_child)
                if furthest_child.pos >= len(self.asteroids):
                    # fin
                    break
            furthest_child.children = furthest_child.get_queue()
            for i in furthest_child.children:
                if i not in self.visited_nodes:
                    self.priority_queue.append(i)
                    break
            print(furthest_child)
        return furthest_child

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

    def get_queue(self):
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
        self.reverse = True
        for dd in self.directions:
            next_pos = self.pos - (self.v + dd)
            if next_pos < 0:
                continue
            if not self.pos_full_next_turn(next_pos):
                vv = self.v + dd
                pos = self.pos - vv
                ss = Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=pos, v=vv, d=dd,
                    t=0, parent=self
                )

                if ss in self.visited_nodes:
                    continue
                out.append(ss)
        return out


def safe(cycle):
    # return True if position is safe
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

    unchangable_ships = []
    for index, speed in gap_list:
        pos = index
        vvv = speed + 1
        ddd = 0
        possible_time = 0
        ss = Ship(
            asteroids=inp['asteroids'],
            t_per_blast_move=inp['t_per_blast_move'],
            p=pos, v=vvv, d=ddd,
            t=possible_time, parent=None
        )

        unchangable_ships.append(ss)

    return unchangable_ships


def choose_closest_route_to_equilibrium(ship, queue):
    if ship.equilibrium > 0:
        child = queue[-1]
    elif ship.equilibrium < 0:
        child = queue[0]
    elif ship.equilibrium == 0:
        child = queue[len(queue) // 2]
    return child


def move_with_equilibrium(ship, unchangable_ships=None):
    # 1, 0, -1
    if not unchangable_ships:
        return ship.move()
    ship.priority_queue = ship.get_queue()
    i = 0
    child = None
    while ship.priority_queue:
        need_to_be_ship = unchangable_ships[i]

        if ship.equilibrium < 0:
            child = ship.priority_queue[0]
        if ship.equilibrium > 0:
            child = ship.priority_queue[-1]
        if ship.equilibrium == 0:
            if len(ship.priority_queue) > 2:
                child = ship.priority_queue[1]
            else:
                child = ship.priority_queue[len(ship.priority_queue)//2]

        # if child not in ship.visited_nodes:
            # ship.visited_nodes.qappend(child)
        if need_to_be_ship:
            if child.pos >= need_to_be_ship.pos:
                i += 1
        print("{c} \t {a}".format(
            c=child,
            a=ship.asteroids[child.pos-1],
            # l=(ship.asteroids[child.pos].get('offset') + child.t + 1) % ship.asteroids[child.pos].get('t_per_asteroid_cycle'),
            # e=unchangable_ships[3:]
        ))

        ship.equilibrium = child.v - need_to_be_ship.v -1
        ship.priority_queue = child.get_queue()

    return child

# inp = {
#   "t_per_blast_move": 10,
#   "asteroids": [
#     {
#       "offset": 0,
#       "t_per_asteroid_cycle": 2
#     },
#     {
#       "offset": 1,
#       "t_per_asteroid_cycle": 3
#     },
#     {
#       "offset": 3,
#       "t_per_asteroid_cycle": 4
#     },
#     {
#       "offset": 1,
#       "t_per_asteroid_cycle": 2
#     }
#   ]
# }

unchangable_ships = find_impossible_gaps(inp['asteroids'])

# def create_reverse_route(unchangable_ships)
#     milestone = unchangable_ships[-1]

#     while milestone:
#         queue = milestone.get_reverse_queue()
#         for ss in queue:
#             if ss in unchangable_ships:
#                 milestone = ss

#         milestone.potential_nodes += queue

#     return milestone

start_ship = Ship(
    inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
    t=0, p=0, v=0, parent=None
)

last_dude = move_with_equilibrium(start_ship, unchangable_ships)
ee = last_dude
sol = []
while last_dude.parent:
    sol.append(last_dude.d)
    last_dude = last_dude.parent

sol.reverse()
print(sol)
print(unchangable_ships)
print("SAFETY IS AT : {0}".format(len(ee.asteroids)))
print('-'*90); import pdb; pdb.set_trace()  # breakpoint 1f449f01  noqa  //
print('donezo')
