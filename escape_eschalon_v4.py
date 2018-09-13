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

    def __repr__(self):
        return "<Ship at {0} v: {1} t: {2} >".format(self.pos, self.v, self.t)

    def __init__(
        self, asteroids=None, t_per_blast_move=None,
        t=None, p=None, v=None, d=None, parent=None
    ):
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
                print('ASTEROIDS DONEEEEE')
                next_pos = len(self.asteroids) - 1
            if not self.pos_full_next_turn(next_pos):
                vv = self.v + dd
                pos = self.pos + vv
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


    # 12561
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
            if next_pos <= need_to_get_to_position:
                print('ASTEROIDS DONEEEEE')
                next_pos = len(self.asteroids) - 1
                return [next_pos]
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
                if reverse:
                    if furthest_child.pos <= need_to_get_to_position:
                        # fin
                        break
                else:
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


def find_last_legal_moves(ship):
    out = []
    cc = 0
    qq = ship.asteroids[ff.pos - 1:]
    qq.reverse()

    while cc < len(qq):
        ast = qq[cc]
        if ast.get('t_per_asteroid_cycle') != 1:
            # because reverse index
            out.append(cc+1)
        cc += 1
    return out
# index of the asteroid that we can jump to, everything else is illegal

need_to_get_to_position = ff.pos
legal_indexes = find_last_legal_moves(ff)
escape_velocity = legal_indexes[0]
last_legal_position = len(ff.asteroids) - legal_indexes[0]
last_ship = Ship(
    inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
    p=last_legal_position, v=escape_velocity, t=0, parent=None
)

last_ship.need_to_get_to_position = need_to_get_to_position
rr = last_ship.move(reverse=True)

asteroids = rr.asteroids[ff.pos:rr.pos]
speed = 0
speed_map = {}

difference = 0
for i in range(0, len(asteroids)):
    ast = asteroids[i]
    cycle = ast.get('t_per_asteroid_cycle')
    if len(speed_map) == 0 and cycle == 1:
        # enter the first value that starts with the illegal move
        speed_map[i-1] = speed
        difference = i-1
        continue
    if cycle == 1:
        speed += 1
    if cycle != 1 and speed == 0:
        continue
    if cycle != 1:
        speed_map[i] = speed
        speed = 0


print('-'*90); import pdb; pdb.set_trace()  # breakpoint 9a49957d  noqa  //
print('donezo')










# while not children:
#     # get the last visited node
#     cutoff_point = ff.visited_nodes[(-1 * (cc + 1))]
#     cutoff_point = cutoff_point.pos
#     leftover = ff.asteroids[cutoff_point:]
#     leftover.reverse()
#     start_ship = Ship(
#         leftover, t_per_blast_move=inp['t_per_blast_move'],
#         a=0, t=0, p=0, v=0, parent=None
#     )
#     children = start_ship.get_queue()

# start_ship.priority_queue += children
# ee = start_ship.move()
# print('-'*90); import pdb; pdb.set_trace()  # breakpoint 1e92ee27  noqa  //


# while ee.parent:
#     if ee.get_queue():
#         ee = ee.move()
#         if cc % 1000 == 0:
#             print(ee)
#             cc = 0
#         else:
#             cc+=1
#     ee = ee.parent

asteroid_count = len(inp['asteroids'])
print("SAFETY IS AT : {0}".format(asteroid_count))
