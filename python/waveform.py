import numpy as np

def interpolate_path(path, samples=50):
    xs, ys = [], []

    for i in range(len(path) - 1):
        x0, y0 = path[i]
        x1, y1 = path[i + 1]

        for t in np.linspace(0, 1, samples):
            xs.append(x0 + (x1 - x0) * t)
            ys.append(y0 + (y1 - y0) * t)

    return np.array(xs), np.array(ys)


def normalize(xs, ys):
    xs = np.array(xs)
    ys = np.array(ys)

    xs = (xs - xs.min()) / (xs.max() - xs.min())
    ys = (ys - ys.min()) / (ys.max() - ys.min())

    # convert to -1..1
    xs = xs * 2 - 1
    ys = ys * 2 - 1

    return xs, ys
