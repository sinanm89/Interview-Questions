import json
# import sys
# sys.setrecursionlimit(3000)
# PYTHON_MAX_RECURSION_LIMIT = 500


class Ship(object):

    blast_position = 0

    solution = []

    def __repr__(self):
        return "<Ship at {0} with {1} v>".format(self.pos, self.v)

    def __init__(
        self, asteroids=None, t_per_blast_move=None,
        a=None, t=None, p=None, v=None, d=None, parent=None
    ):
        # self.visited = []
        self.visited = False
        self.a = a
        self.priority_queue = []
        self.d = d
        self.t = t
        self.v = v
        self.pos = p
        self.parent = parent
        self.asteroids = asteroids
        self.t_per_blast_move = t_per_blast_move
        self.safety_distance = len(self.asteroids)

    def __lt__(self, other):
        return self.pos < other.pos

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
            if next_pos >= len(self.asteroids):
                return 'end'
            if next_pos in visited:
                continue
            if not self.pos_full_next_turn(next_pos):
                vv = self.v + dd
                pos = self.pos + vv
                ss = Ship(
                    asteroids=self.asteroids,
                    t_per_blast_move=self.t_per_blast_move,
                    p=pos, v=vv, d=dd,
                    t=self.t + 1, parent=self
                )
                out.append(ss)
        return out

    def pos_full_next_turn(self, pos):
        ast = self.asteroids[pos - 1]
        cycle = ast.get('t_per_asteroid_cycle')
        if (ast.get('offset') + self.t + 1) % cycle == 0:
            return True
        return False


def backtrack_until_move_avail(ship, visited=[]):
    # prev_ship_pos = ship.pos
    queue = ship.get_queue(visited=visited)
    # visited.append(ship.parent)
    visited.sort()
    while queue:
        qq = queue.pop(0)
        # because we tried the bigger value and it didnt work
        if visited and qq.pos >= visited[0]:
            continue
        if qq.get_queue(visited=visited):
            # this can move
            break
    else:
        visited = [ship.pos]
        qq = backtrack_until_move_avail(ship.parent, visited)
    return qq


def move(ship):
    queue = ship.get_queue()
    queue.sort(reverse=True)
    while queue and ship.pos < len(ship.asteroids):
        if queue == 'end':
            return ship
        child = queue.pop(0)
        child.parent = ship
        child.t = ship.t + 1
        if child.get_queue():
            ship.solution.append(child.d)
            return move(child)
        else:
            continue
    return move(backtrack_until_move_avail(ship.parent, [ship.pos]))

with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
ship = Ship(
    inp['asteroids'].reverse(), t_per_blast_move=inp['t_per_blast_move'],
    a=0, t=0, p=0, v=0, parent=None
)
queue = ship.get_queue()
ship.priority_queue += queue
ship.priority_queue.sort(reverse=True)
asteroid_count = len(inp['asteroids'])
print("SAFETY IS AT : {0}".format(asteroid_count))

ship = move(ship)

out = []
while ship.parent:
    # print(ship.d)
    out.append(ship.d)
    ship = ship.parent
out.reverse()
print out
