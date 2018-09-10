# t_per_asteroid_cycle = time it takes to make one full cycle

# if v > 1 , cant hit asteroid if new space is empty.

# - sort by offset

inp = {
    "asteroids": [
        {
            "t_per_asteroid_cycle": 3,
            "offset": 0
        },
        {
            "t_per_asteroid_cycle": 2,
            "offset": 1
        },
        {
            "t_per_asteroid_cycle": 1,
            "offset": 2
        },
    ],
    "t_per_blast_move": 2
}


def merge(left, right):
    out = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        l_check = left[i]['offset']
        r_check = right[j]['offset']
        if l_check > r_check:
            out.append(right[j])
            j += 1
        elif l_check < r_check:
            out.append(left[i])
            i += 1
    out += left[i:]
    out += right[j:]
    return out


def merge_sort(arr):
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

    def __init__(self, asteroids):
        self.asteroids = merge_sort(inp['asteroids'])
        max_offset = self.asteroids[-1].get('offset')
        asteroid_map = {}
        # map asteroids by offset/position
        for i in self.asteroids:
            asteroid_map[i.get('offset')] = asteroid_map.get(i.get('offset'), [])
            asteroid_map[i.get('offset')].append(i.get('offset'))

    def acc(self):
        self.a += 1
        return self.v + self.a

    def dec(self):
        self.a += 1
        return self.v - self.a

    def is_offset_full(t, offset):
        asteroids = self.asteroid_map.get(offset)
        for ast in asteroids:
            one_cycle = ast.get('t_per_asteroid_cycle')
            if t % one_cycle == 0:
                return True
        return False

    def potential_positions(self):
        # the highest weighted diretion is accelating forwards
        # since were getting closer to the safezone
        directions = [1, 0, -1]
        return [(self.pos + self.v + self.a + d) for d in directions]

    def move(self):
        # look at possible movements
        # calculate the overall cost
        # add all routes to priority queue
        # choose the smallest one.
        # keep in mind the direction

        # nlogn complexity

        maybe_move = []

        current_t = 0
        current_offset_asteroids = []
        prev_offset = ordered_by_distance_asteroids[0].get('offset')

        blast_position = 0

        def blast_zone(current_t, blast_position):
            if current_t % t_per_blast_move == 0:
                blast_position += t_per_blast_move
            return blast_position

        # position_movement_weight = positions_offset + v + a
        for i in self.asteroids:
            next_pos = []
            if prev_offset != i.get('offset'):

                # we have all the asteroids on pos
                if is_offset_full(t, current_offset_asteroids):
                    # check legal move
                    if maybe_move:
                        # if we have a legal move where we can go forward or backward
                    else:
                        pass
                        # wait 1 time without changing position for asteroids to pass
                # calculate the next move costs
            else:
                current_offset_asteroids.append(i)
            prev_offset = i.get('offset')


ship = Ship(inp)
