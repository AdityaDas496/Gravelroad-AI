import time
from violations.parking_zone import inside_parking_zone

parking_history = {}

YELLOW_THRESHOLD = 5
RED_THRESHOLD = 10

MOVEMENT_THRESHOLD = 40


def get_parking_status(track_id, x, y):

    if not inside_parking_zone(x, y):

        parking_history.pop(track_id, None)
        return "normal"

    current_time = time.time()

    if track_id not in parking_history:

        parking_history[track_id] = {
            "start_x": x,
            "start_y": y,
            "start_time": current_time
        }

        return "normal"

    start_x = parking_history[track_id]["start_x"]
    start_y = parking_history[track_id]["start_y"]

    total_distance = (
        ((x - start_x) ** 2) +
        ((y - start_y) ** 2)
    ) ** 0.5

    # Vehicle has genuinely moved
    if total_distance > MOVEMENT_THRESHOLD:

        parking_history[track_id] = {
            "start_x": x,
            "start_y": y,
            "start_time": current_time
        }

        return "normal"

    parked_time = (
        current_time -
        parking_history[track_id]["start_time"]
    )

    if parked_time >= RED_THRESHOLD:
        return "red"

    if parked_time >= YELLOW_THRESHOLD:
        return "yellow"

    return "normal"