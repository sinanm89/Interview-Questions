import json
import sys
sys.setrecursionlimit(3000)
# PYTHON_MAX_RECURSION_LIMIT = 500


class Ship(object):

    blast_position = 0

    solution = None
    potential_moves = []
    visited_nodes = []

    def __repr__(self):
        return "<Ship at {0} with {1} v>".format(self.pos, self.v)

    def __init__(
        self, asteroids=None, t_per_blast_move=None,
        a=None, t=None, p=None, v=None, d=None, parent=None
    ):
        self.d = d
        self.t = t
        self.v = v
        self.pos = p
        self.parent = parent
        self.asteroids = asteroids
        self.t_per_blast_move = t_per_blast_move
        self.safety_distance = len(self.asteroids)

    def __lt__(self, other):
        return self.weight() < other.weight()

    def __eq__(self, other):
        sss = {
            "v": self.v, "t": self.t, "pos": self.pos
        }
        other = {
            "v": other.v, "t": other.t, "pos": other.pos
        }
        return sss == other

    def weight(self):
        return self.pos + self.v + self.t

    def blast_zone_check(self):
        if (
            self.pos <= self.blast_position and
            self.blast_position != 0 and
            self.pos < 0
        ):
            print('blown to bits at pos: {0} and blast pos :{1}'.format(
                self.pos, self.blast_position))
            return False
        if self.t > 0 and self.t % self.t_per_blast_move == 0:
            self.blast_position += self.t_per_blast_move
        return True

    def get_queue(self, visited=[]):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        directions = [1, 0, -1]
        # position_movement_weight = positions_offset + v + a + d
        out = []
        for dd in directions:
            next_pos = self.pos + self.v + dd
            if not self.pos_full_next_turn(next_pos):
                vv = self.v + dd
                pos = self.pos + vv
                ss = Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=pos, v=vv, d=dd,
                    t=self.t + 1, parent=self
                )
                if not(ss in self.visited_nodes):
                    out.append(ss)
        return out

    def pos_full_next_turn(self, pos):
        ast = self.asteroids[pos - 1]
        cycle = ast.get('t_per_asteroid_cycle')
        if (ast.get('offset') + self.t + 1) % cycle == 0:
            return True
        return False


# def backtrack_until_move_avail(ship, visited=[]):
#     queue = ship.get_queue(visited=visited)
#     visited.sort()
#     while queue:
#         qq = queue.pop(0)
#         # because we tried the bigger value and it didnt work
#         # if qq.pos >= visited[0]:
#             # continue
#         if qq.get_queue(visited=visited):
#             # this can move
#             break
#     else:
#         qq = backtrack_until_move_avail(ship.parent, [ship.pos])
#     return qq


def move(ship, prev=None):
    queue = ship.get_queue()
    queue.sort()
    if ship not in ship.visited_nodes:
        ship.visited_nodes.append(ship)
    if ship.pos >= len(ship.asteroids):
        return ship
    while queue and ship.pos < len(ship.asteroids):
        child = queue.pop()
        child.parent = ship
        child.t = ship.t + 1
        for i in child.get_queue():
            if i in ship.visited_nodes or len(i.get_queue()) == 0:
                continue
            elif i not in ship.potential_moves:
                ship.potential_moves.append(i)
    return ship

with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
ship = Ship(
    inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
    a=0, t=0, p=0, v=0, parent=None
)

asteroid_count = len(inp['asteroids'])
print("SAFETY IS AT : {0}".format(asteroid_count))

ship = move(ship)
ship.visited_nodes = []


def update_pot_moves(ship):
    temp_pot_moves = []
    for ee in ship.potential_moves:
        for i in ee.get_queue():
            if i in ship.visited_nodes or len(i.get_queue()) == 0:
                continue
            elif i not in temp_pot_moves:
                temp_pot_moves.append(i)
    ship.potential_moves = temp_pot_moves
    if ship.t > 140:
        print('-'*90); import pdb; pdb.set_trace()  # breakpoint 4aa85a71  noqa  //

    # ship.potential_moves.sort(reverse=True)
    ship.potential_moves.sort()
    # ship.potential_moves = sorted(ship.potential_moves, key=lambda w: w.weight())   # sort by weight
    return ship

while ship.potential_moves:
    ship = move(ship.potential_moves.pop())
    ship = update_pot_moves(ship)

        # for i in ship.potential_moves:
        #     for j in ship.potential_moves:
        #         if i.pos == j.pos and i.v == j.v:

out = []
while ship.parent:
    # print(ship.d)
    out.append(ship.d)
    ship = ship.parent
out.reverse()
print(out)
