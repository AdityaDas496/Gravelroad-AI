import supervision as sv

tracker = sv.ByteTrack(lost_track_buffer=90, minimum_matching_threshold=0.9)

def update_tracks(detections):
    return tracker.update_with_detections(detections)