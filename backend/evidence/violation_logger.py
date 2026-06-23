import csv
import os
from datetime import datetime

CSV_FILE = "violations.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["vehicle_id", "violation_type", "timestamp", "evidence_path"])

def log_violation(track_id, violation_type, evidence_path):
    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([track_id, violation_type, datetime.now(), evidence_path])