import re

def relative_position(p, q):
    if p > q:
        return -1
    elif p < q:
        return 1
    else:
        return 0

def apply_gravity(positions, velocities):
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

def update_position(positions, velocities):
    N = len(positions)
    for i in range(N):
        [vx, vy, vz] = velocities[i]
        [px, py, pz] = positions[i]
        positions[i] = (px + vx, py + vy, pz + vz)

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
    nsteps = 1000
    positions = []
    for inp in input:
        coordinates = re.search("<x=(-*[0-9]*),\s*y=(-*[0-9]*),\s*z=(-*[0-9]*)>", inp)
        positions.append((int(coordinates.group(1)),
                          int(coordinates.group(2)),
                          int(coordinates.group(3))))
    N = len(positions)
    velocities = [(0, 0, 0) for _ in range(N)]
    run_simulation(positions, velocities, nsteps)
    total_energy = total_energy(positions, velocities)
    print('Final positions = {}'.format(positions))
    print('Final velocities = {}'.format(velocities))
    print('Total energy = {}'.format(total_energy))
