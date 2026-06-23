vehicle_history = {}

def check_wrong_side(track_id, center_x, center_y):
    if track_id not in vehicle_history:
        vehicle_history[track_id] = (center_x, center_y)
        return False

    prev_x, prev_y = vehicle_history[track_id]
    vehicle_history[track_id] = (center_x, center_y)
    dy = center_y - prev_y
    # If going opposite side than other cars then wrong
    if dy < -5:
        return True
    return False