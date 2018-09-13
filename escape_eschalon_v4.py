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
        a=None, t=None, p=None, v=None, d=None, parent=None
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

    def move(self):
        self.priority_queue = self.get_queue()
        while self.priority_queue:
            furthest_child = self.priority_queue.pop()
            if furthest_child not in self.visited_nodes:
                self.visited_nodes.append(furthest_child)
                if furthest_child.pos >= len(self.asteroids):
                    # fin
                    break
            furthest_child.children = furthest_child.get_queue()
            for i in furthest_child.children:
                if i not in self.visited_nodes:
                    self.priority_queue.append(i)
                    self.priority_queue = list(set(self.priority_queue))
                    break
                # for i in furthest_child.children:
                # if i not in self.visited_nodes:
                #     ee = set(self.priority_queue)
                #     ee.add(i)
                #     self.priority_queue = list(ee)
        return furthest_child


# set(self.priority_queue).subtract(set(self.visited_nodes))

with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
start_ship = Ship(
    inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
    a=0, t=0, p=0, v=0, parent=None
)
children = start_ship.get_queue()
start_ship.children = children
start_ship.priority_queue += children
ee = start_ship.move()
ee.directions = [-1, 0, 1]
cc = 0

while ee.parent:
    if ee.get_queue():
        ee = ee.move()
        if cc % 400 == 0:
            print(ee)
            cc = 0
        else:
            cc+=1
    ee = ee.parent

asteroid_count = len(inp['asteroids'])
print("SAFETY IS AT : {0}".format(asteroid_count))
