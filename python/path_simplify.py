import numpy as np

def douglas_peucker(points, epsilon=2.5):
    if len(points) < 3:
        return points

    start, end = np.array(points[0]), np.array(points[-1])

    line = end - start
    line_len = np.linalg.norm(line)

    if line_len == 0:
        return [points[0], points[-1]]

    distances = []
    for p in points:
        p = np.array(p)
        proj = start + np.dot(p - start, line) / line_len**2 * line
        dist = np.linalg.norm(p - proj)
        distances.append(dist)

    max_idx = np.argmax(distances)
    max_dist = distances[max_idx]

    if max_dist > epsilon:
        left = douglas_peucker(points[:max_idx], epsilon)
        right = douglas_peucker(points[max_idx:], epsilon)
        return left[:-1] + right
    else:
        return [points[0], points[-1]]
