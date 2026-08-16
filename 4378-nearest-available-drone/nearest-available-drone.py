class Solution:
    def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
        
        idx = -1
        mini = float('inf')

        a, b = target

        for i in range(len(drones)):
            x, y, z = drones[i]

            m_dist = abs(x - a) + abs(y - b)

            if m_dist <= z and m_dist < mini:
                mini = m_dist
                idx = i

        return idx