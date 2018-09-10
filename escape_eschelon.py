import json

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
#             "offset": 4,
#             "t_per_asteroid_cycle": 2
#         }
#     ]
# }


def merge(left, right):
    out = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        l_check = left[i]['offset']
        r_check = right[j]['offset']
        if l_check > r_check:
            out.append(right[j])
            j += 1
        else:
            out.append(left[i])
            i += 1
    out += left[i:]
    out += right[j:]
    return out


def merge_sort(arr):
    # pythons internal .sort does timsort which is similar to this,
    # their avg complexity is both nlogn.

    # // floors float val to int
    mid = len(arr) // 2
    if len(arr) <= 2:
        l_check = arr[0].get('offset')
        r_check = arr[-1].get('offset')

        # last element check doesnt throw index error when len(arr)==1
        if l_check > r_check:
            arr[-1], arr[0] = arr[0], arr[-1]
        return arr
    return merge(merge_sort(arr[:mid]), merge_sort(arr[mid:]))


class Ship(object):

    v = 0
    a = 0
    pos = 0
    t = 0
    blast_position = 0

    solution = []

    def __init__(self, data):
        self.asteroids = merge_sort(data['asteroids'])
        self.t_per_blast_move = data.get('t_per_blast_move')
        self.max_offset = self.asteroids[-1].get('offset')
        print("MAX OFFSET IS : {0}".format(self.max_offset))
        self.asteroid_map = {}
        # map asteroids by offset/position
        for i in self.asteroids:
            if not self.asteroid_map.get(i.get('offset'), False):
                self.asteroid_map[i.get('offset')] = []
            self.asteroid_map[i.get('offset')].append(i)

    def potential_positions(self):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        directions = [1, 0, -1]
        # position_movement_weight = positions_offset + v + a + d
        return [(self.pos + self.v + d) for d in directions]

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

    def is_offset_full_next_turn(self, offset):
        # get the astroids of offset
        asteroids = self.asteroid_map.get(offset, [])
        if len(asteroids) < 1:
            return False
        for ast in asteroids:
            if (self.t + 1) % ast.get('t_per_asteroid_cycle') == 0:
                return True
        return False

    def move(self):
        if self.pos >= self.max_offset:
            return self.solution
        if not self.blast_zone_check():
            return False
        maybe_move = self.potential_positions()
        while maybe_move:
            next_pos = maybe_move.pop(0)
            print('-'*90); import pdb; pdb.set_trace()  # breakpoint 91ff27e1  noqa  //

            if not self.is_offset_full_next_turn(next_pos):
                # update ship values
                # move 1 t
                self.a = next_pos - (self.pos + self.v)
                print("t: {0} p: {1} v: {2} a: {3}".format(
                    self.t, self.pos, self.v, self.a))
                self.v += self.a
                self.pos = next_pos
                self.t += 1
                self.solution.append(self.a)
                return self.move()
        return False

with open("v3_chart.json") as f:
    data = f.read()

inp = json.loads(data)
ship = Ship(inp)
ship.move()
print(ship.solution)
