from capture import get_frame
from vectorize import get_edges, extract_contours
from path_simplify import douglas_peucker
from waveform import interpolate_path, normalize
from serial_stream import XYStreamer

import cv2

streamer = XYStreamer(port="COM3")

def process_frame(frame):
    edges = get_edges(frame)
    contours = extract_contours(edges)

    all_x, all_y = [], []

    for c in contours:
        c = douglas_peucker(c, epsilon=2.0)
        xs, ys = interpolate_path(c, samples=20)

        xs, ys = normalize(xs, ys)

        all_x.extend(xs)
        all_y.extend(ys)

    return all_x, all_y, edges


def main():
    print("Starting oscilloscope renderer...")

    while True:
        frame = get_frame()

        xs, ys, edge_img = process_frame(frame)

        streamer.send(xs, ys)

        cv2.imshow("Edges", edge_img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
