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

def apply_gravity_3d(positions, velocities):
    for i, pi in enumerate(positions):
        del_vx = 0
        del_vy = 0
        del_vz = 0
        for j, pj in enumerate(positions):
            if pi != pj:
                del_vx += relative_position(pi[0], pj[0])
                del_vy += relative_position(pi[1], pj[1])
                del_vz += relative_position(pi[2], pj[2])
        [vx, vy, vz] = velocities[i]
        velocities[i] = (vx + del_vx, vy + del_vy, vz + del_vz)

def apply_gravity_1d(positions, velocities):
    N = len(positions)
    for i in range(N):
        del_v = 0
        for j in range(N):
            if positions[i] != positions[j]:
                del_v += relative_position(positions[i], positions[j])
        velocities[i] += del_v

def update_position_3d(positions, velocities):
    N = len(positions)
    for i in range(N):
        [vx, vy, vz] = velocities[i]
        [px, py, pz] = positions[i]
        positions[i] = (px + vx, py + vy, pz + vz)


def update_position_1d(positions, velocities):
    N = len(positions)
    for i in range(N):
        positions[i] += velocities[i]

def run_simulation(N, positions, velocities, nsteps):
    for _ in range(nsteps):
        apply_gravity_3d(positions, velocities)
        update_position_3d(positions, velocities)

def total_energy(N, positions, velocities):
    total_energy = 0
    for i in range(N):
        [vx, vy, vz] = velocities[i]
        [px, py, pz] = positions[i]
        total_energy += (abs(vx) + abs(vy) + abs(vz)) * \
                        (abs(px) + abs(py) + abs(pz))
    return total_energy

def get_positions_from_input(input):
    positions = []
    for inp in input:
        coordinates = re.search("<x=(-*[0-9]*),\s*y=(-*[0-9]*),\s*z=(-*[0-9]*)>", inp)
        positions.append((int(coordinates.group(1)),
                          int(coordinates.group(2)),
                          int(coordinates.group(3))))
    return positions

def init_simulation(input):
    positions = get_positions_from_input(input)
    N = len(positions)
    velocities = [(0, 0, 0) for _ in range(N)]
    return N, positions, velocities


def find_duplicate_state(N, positions, velocities):
    N = len(positions)
    steps = [0, 0, 0]
    for dim in range(3):
        visited_states = set()
        pos_d = [p[dim] for p in positions]
        vel_d = [v[dim] for v in velocities]
        visited_states.add(tuple(pos_d))
        steps_d = 1
        while 1:
            apply_gravity_1d(pos_d, vel_d)
            update_position_1d(pos_d, vel_d)
            state = tuple(pos_d)
            steps_d += 1
            if state in visited_states:
                steps[dim] = steps_d
                break
    return lcm(lcm(steps[0], steps[1]), steps[2])

if __name__ == '__main__':
    file = open('day12_input.txt', 'r')
    input = file.read().split('\n')[:-1]

    # part a
    nsteps = 1000
    N, positions, velocities = init_simulation(input)
    run_simulation(N, positions, velocities, nsteps)
    total_energy = total_energy(N, positions, velocities)
    print('Final positions = {}'.format(positions))
    print('Final velocities = {}'.format(velocities))
    print('Total energy = {}'.format(total_energy))

    # part b
    N, positions, velocities = init_simulation(input)
    steps = find_duplicate_state(N, positions, velocities)
    print('Steps required to reach first duplicate state = {}'.format(steps))
