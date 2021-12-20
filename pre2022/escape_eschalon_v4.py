# -*- coding: utf-8 -*-
"""Escape from Eschaton: Altschool Interview Question.

Ive written a type of dynamiccally changing aStar algorithm where the
worst case solution for this problem would be O(n) where n is the number
of asteroids. The best case would be O(m) where m<n and m is the maximum
number of jumps necessary to leave the asteroid belt of length n.

Example:
    To run the script, use the following format, it searches for a file
    called v3_chart.json unless a file is specified::

        $ python escape_eshaton.py filename.json
        $ python escape_eshaton.py

The json file should be in the following format::

    {
        "asteroids": [
            {
                "t_per_asteroid_cycle": 2,
                "offset": 0
            }
        ],
        "t_per_blast_move": 2
    }

.. _Problem Documentation & Examples
    https://goo.gl/JYShwB
"""
import json
import sys
import logging


class Ship(object):
    """Ship object that holds the states of the map and potential moves.
    """

    blast_position = 0
    t_per_blast_move = 0
    asteroids = []

    unchangable_ships = []
    visited_nodes = []
    priority_queue = []

    directions = [1, 0, -1]

    equilibrium = 0

    def __repr__(self):
        """The string representation of the object."""
        return "<Ship at {0} v: {1} t: {2} >".format(
            self.pos, self.v, self.t
        )

    def __init__(
        self, asteroids=None, t_per_blast_move=None,
        t=None, p=None, v=None, d=None, parent=None
    ):
        """Individual and general ship attribute initializer.

        Args:
            asteroids (list, optional): A shared list of all the
                asteroids.
            t_per_plast_move (int, optional): Shared cycle when the
                blast moves forward once.
            t (int, optional): Instance turn counter.
            p (int, optional): Instance position.
            v (int, optional): Instance speed.
            d (int, optional): Instance acceleration for the given turn.
            parent (:obj: `Ship`, optional): The second parameter.

        """
        self.asteroids = asteroids
        self.t_per_blast_move = t_per_blast_move
        self.d = d
        self.t = t
        self.v = v
        self.pos = p
        self.parent = parent

    def __eq__(self, other):
        """Internal python object method for comparisons."""
        return (self.pos, self.v) == (other.pos, other.v)

    def pos_full_next_turn(self, pos):
        """Check if the position is available next turn.

        Args:
            pos (int): position of asteroid on the self.asteroids list.

        Returns:
            bool: True if position is full False otherwise.
        """
        ast = self.asteroids[pos - 1]
        cycle = ast.get('t_per_asteroid_cycle')
        if (ast.get('offset') + self.t + 1) % cycle == 0:
            return True
        return False

    def blast_zone_check(self, pos, t):
        """
        Check to see if the planet explosion envelops the ship at pos.
        As well as increment the blast zone. This gets called every
        loop.

        Args:
            pos (int): position to check.
            t (int): time at position.

        Returns:
            bool: True if blast zone is secure. False otherwise.
        """
        if (
            pos <= self.blast_position and
            self.blast_position != 0 and
            pos < 0
        ):
            return False
        if t > 0 and t % self.t_per_blast_move == 0:
            self.blast_position += self.t_per_blast_move
        return True

    def get_queue(self):
        """Next move getter. Takes into account different conditions for
        a valid move return.

        Returns:
            list (:obj, `Ship`): A list of ships ordered by directions.
        """
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

    def find_impossible_gaps(self):
        """A map can have impossible to pass terrains. Since finding
        every permutation will be costly we only look through the
        non-cycling asteroids.
        """
        speed = 0
        self.unchangable_ships = []

        def safe(cycle):
            # return True if position is safe
            return cycle != 1

        for i in range(0, len(self.asteroids)):
            ast = self.asteroids[i]
            cycle = ast.get('t_per_asteroid_cycle')
            if not safe(cycle) and speed == 0:
                # impossibility start
                speed += 1
            elif not safe(cycle) and speed != 0:
                # impossibility in progress
                speed += 1
            if safe(cycle) and speed != 0:
                # impossibility end
                start_index = i - (speed + 1)
                self.unchangable_ships.append((start_index, speed + 1))
                speed = 0
            elif safe(cycle):
                # safe
                speed = 0
        if speed != 0:
            # if impossibility is inevitable, set the end.
            start_index = i - speed
            self.unchangable_ships.append((start_index, speed + 1))

    def move_with_equilibrium(self):
        """Move the ship in regards to the impossible gaps, once a
        gap is passed look for the next. Adjust speed according to the
        relative position from impossibility.

        Returns:
            :obj: `Ship`: the last possible move of a ship.
        """
        self.find_impossible_gaps()
        self.priority_queue = self.get_queue()
        queue = self.priority_queue
        i = 0
        child = None

        while self.priority_queue:
            if self.unchangable_ships:
                need_to_be_ship = self.unchangable_ships[i]
            if queue:
                # try to go forward from the child for a direct approach
                if self.equilibrium < 0:
                    child = queue[0]
                if self.equilibrium > 0:
                    child = queue[-1]
                if self.equilibrium == 0:
                    # we try to move to the middle or lesser position
                    child = queue[len(queue) // 2]
            else:
                # pick the furthest available position thats not visited
                child = self.priority_queue.pop()

            if child.pos >= len(self.asteroids) - 1:
                break

            if child not in self.visited_nodes:
                self.visited_nodes.append(child)
            if need_to_be_ship:
                if (
                    child.pos >= need_to_be_ship[0] and
                    i < len(self.unchangable_ships)
                ):
                    i += 1
            logging.debug("{c} \t {a} \t {e}".format(
                c=child,
                a=self.asteroids[child.pos - 1],
                e=self.equilibrium,
            ))
            self.equilibrium = child.v - need_to_be_ship[1]
            queue = child.get_queue()
            self.priority_queue += queue
        return child


def main():
    """Main runner."""
    logging.basicConfig(level=logging.INFO)

    if len(sys.argv[1:]) > 0:
        filename = sys.argv[1]
    else:
        filename = "v3_chart.json"
    try:
        with open(filename) as f:
            data = f.read()
        inp = json.loads(data)
    except IOError:
        raise IOError('File doesnt exist. Perhaps try `v3_chart.json`?')
    except:
        raise Exception('Something terrible has happened.')

    start_ship = Ship(
        inp['asteroids'], t_per_blast_move=inp['t_per_blast_move'],
        t=0, p=0, v=0, parent=None
    )

    last_ship = start_ship.move_with_equilibrium()
    last_ship_pos = last_ship.pos
    solution = []
    while last_ship.parent:
        solution = [last_ship.d] + solution
        last_ship = last_ship.parent
    logging.info(solution)

    if last_ship_pos >= len(last_ship.asteroids):
        return logging.info(True)
    return logging.info(False)

if __name__ == '__main__':
    main()
