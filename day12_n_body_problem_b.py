import re
from fractions import gcd
import time

def lcm(x, y):
   lcm = (x * y) // gcd(x, y)
   return lcm

def relative_position(p, q):
    if p > q:
        return -1
    elif p < q:
        return 1
    else:
        return 0

def apply_gravity(positions, velocities):
    N = len(positions)
    for i in range(N):
        del_v = 0
        for j in range(N):
            if positions[i] != positions[j]:
                del_v += relative_position(positions[i], positions[j])
        velocities[i] += del_v

def update_position(positions, velocities):
    N = len(positions)
    for i in range(N):
        positions[i] += velocities[i]

def find_duplicate_state(positions, velocities):
    N = len(positions)
    steps = [0, 0, 0]
    for dim in range(3):
        visited_states = set()
        pos_d = [p[dim] for p in positions]
        vel_d = [v[dim] for v in velocities]
        visited_states.add(tuple(pos_d))
        steps_d = 1
        while 1:
            apply_gravity(pos_d, vel_d)
            update_position(pos_d, vel_d)
            state = tuple(pos_d)
            steps_d += 1
            if state in visited_states:
                steps[dim] = steps_d
                break
    return lcm(lcm(steps[0], steps[1]), steps[2])

def run_simulation(positions, velocities, nsteps):
    N = len(positions)
    for _ in range(nsteps):
        apply_gravity(positions, velocities)
        update_position(positions, velocities)

def total_energy(positions, velocities):
    total_energy = 0
    N = len(positions)
    for i in range(N):
        [vx, vy, vz] = velocities[i]
        [px, py, pz] = positions[i]
        total_energy += (abs(vx) + abs(vy) + abs(vz)) * \
                        (abs(px) + abs(py) + abs(pz))
    return total_energy

if __name__ == '__main__':
    file = open('day12_input.txt', 'r')
    input = file.read().split('\n')[:-1]
    positions = []
    for inp in input:
        coordinates = re.search("<x=(-*[0-9]*),\s*y=(-*[0-9]*),\s*z=(-*[0-9]*)>", inp)
        positions.append((int(coordinates.group(1)),
                          int(coordinates.group(2)),
                          int(coordinates.group(3))))
    N = len(positions)
    velocities = [(0, 0, 0) for _ in range(N)]
    steps = find_duplicate_state(positions, velocities)
    print('Steps required = {}'.format(steps))
