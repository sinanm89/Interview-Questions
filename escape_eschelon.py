from copy import copy
import json

PYTHON_MAX_RECURSION_LIMIT = 1000

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
    a = 0
    pos = 0
    t = 0
    blast_position = 0

    solution = []
    visited = []

    def __repr__(self):
        return "<Ship at {0} with {1} v>".format(self.pos, self.v)

    def __init__(self, data):
        self.asteroids = data['asteroids']
        self.t_per_blast_move = data.get('t_per_blast_move')
        self.safety_distance = len(self.asteroids)
        print("SAFETY IS AT : {0}".format(self.safety_distance))

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

    def try_to_move(self):
        queue = self.potential_positions()

        if self.pos >= self.safety_distance:
            return True
        # if in blast
        if not self.blast_zone_check():
            return False

        if len(queue) == 0:

            self.solution.pop()
            return self.parent.try_to_move()

        if queue[0] == 'end':
            self.solution.append(queue[-1])
            print(self.solution)
            return True
        return self.move(queue)

    def move(self, queue):
        for next_pos in queue:
            # not full and not visited node
            # if next_pos == 'end':
            #     self.solution.append(queue[-1])
            #     print(self.solution)
            #     return True
            child = copy(self)
            child.visited = []
            child.t += 1
            child.pos = next_pos
            child.v = next_pos - self.pos
            d = next_pos - self.pos - self.v
            self.solution.append(d)

            child.parent = self
            child.parent.visited.append(next_pos)

            return child.try_to_move()
    # def move(self):
    #     if self.pos >= self.max_offset:
    #         return self.solution
    #     if not self.blast_zone_check():
    #         return False

    #     maybe_move = self.potential_positions()
    #     print("t: {0} p: {1} v: {2} a: {3}\nvisited:{4} ".format(
    #         self.t, self.pos, self.v, maybe_move, self.visited))

    #     self.parent = copy(self)
    #     for next_pos in maybe_move:
    #         if not self.is_pos_full_next_turn(next_pos):
    #             a = next_pos - (self.pos + self.v)
    #             # print("t: {0} p: {1} v: {2} a: {3}".format(
    #             #     self.t, self.pos, self.v, a))
    #             self.v += a
    #             self.pos = next_pos
    #             self.t += 1
    #             self.solution.append(a)
    #             self.parent.visited.append(next_pos)
    #             return self.move()

    #     self.parent.t -= 1
    #     self.parent.visited.append(self.pos)
    #     self.parent.pos = self.parent.pos - self.parent.v
    #     self.parent.v = self.parent.v - self.parent.solution.pop()

    #     return self.parent.move()


with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
ship = Ship(inp)
ee = ship.try_to_move()
print(ee)
