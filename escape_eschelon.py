from copy import copy
import json

PYTHON_MAX_RECURSION_LIMIT = 500

inp = {
    "asteroids": [
        {
            "t_per_asteroid_cycle": 3,
            "offset": 0
        },
        {
            "t_per_asteroid_cycle": 3,
            "offset": 1
        },
        {
            "t_per_asteroid_cycle": 2,
            "offset": 4
        },
        {
            "t_per_asteroid_cycle": 2,
            "offset": 3
        },
    ],
    "t_per_blast_move": 2
}
# inp = {
#     "t_per_blast_move": 10,
#     "asteroids": [
#         {
#             "offset": 0,
#             "t_per_asteroid_cycle": 2
#         },
#         {
#             "offset": 1,
#             "t_per_asteroid_cycle": 3
#         },
#         {
#             "offset": 3,
#             "t_per_asteroid_cycle": 4
#         },
#         {
#             "offset": 1,
#             "t_per_asteroid_cycle": 2
#         }
#     ]
# }


class Ship(object):

    v = 0
    pos = 0
    t = 0
    blast_position = 0

    solution = []
    visited = []

    parent = None

    def __repr__(self):
        return "<Ship at {0} with {1} v>".format(self.pos, self.v)

    def __init__(self, data):
        self.asteroids = data['asteroids']
        self.t_per_blast_move = data.get('t_per_blast_move')
        self.safety_distance = len(self.asteroids)
        print("SAFETY IS AT : {0}".format(self.safety_distance))

    def get_queue(self):
        return list(set(self.queue or []) - set(self.visited))

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

    def potential_positions(self):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        directions = [1, 0, -1]
        # position_movement_weight = positions_offset + v + a + d
        out = []
        for d in directions:
            next_pos = self.pos + self.v + d
            if next_pos in self.visited:
                continue
            if next_pos >= len(self.asteroids):
                return ['end', d]
            if not self.pos_full_next_turn(next_pos):
                out.append((self.pos + self.v + d))
        return out

    def pos_full_next_turn(self, pos):
        # get the astroids of offset
        ast = self.asteroids[pos - 1]
        cycle = ast.get('t_per_asteroid_cycle')
        if (ast.get('offset') + self.t + 1) % cycle == 0:
            return True
        return False

    def has_moves(self):
        if len(self.visited) < 3:
            return True
        return False

    def try_to_move(self):
        self.queue = self.potential_positions()

        if self.pos >= self.safety_distance:
            return 'safe'
        # if in blast
        if not self.blast_zone_check():
            return 'dead'

        if len(self.queue) == 0:
            # self.solution.pop()
            parent = self.parent
            while not parent.get_queue():
                parent = parent.parent
            print(parent.get_queue())
            return parent.move()

        if self.queue[0] == 'end':
            self.solution.append(self.queue[-1])
            print(self.solution)
            return True
        return self.move()

    def move(self):
        for next_pos in self.get_queue():
            # not full and not visited node
            # if next_pos == 'end':
            #     self.solution.append(queue[-1])
            #     print(self.solution)
            #     return True
            # child = copy(self)
            child = self
            child.visited = []
            child.t += 1
            child.pos = next_pos
            child.v = next_pos - self.pos
            d = next_pos - self.pos - self.v
            self.solution.append(d)
            self.visited.append(next_pos)
            child.parent = self.parent
            return child.try_to_move()

with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
ship = Ship(inp).try_to_move()

print("pos {pos} v:{v} turn: {t}>".format(pos=ship.pos, v=ship.v, t=ship.t))
# while type(ship) == Ship:
#     turn_count = len(ship.solution)
#     visited = ship.visited
#     ship = Ship(inp)
#     for a in ship.solution:
#         prev_state = copy(ship)
#         ship.t += 1
#         ship.v += a
#         ship.pos += ship.v
#         ship.parent = prev_state
#     ship.visited = visited
#     print(ship.pos)
#     ship = ship.try_to_move(0)

