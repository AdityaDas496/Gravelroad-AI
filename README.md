# Gravelroad AI
<img src="Gravelroad logo.png" alt="System Architecture" width="10%" style="max-width: 10%; height: auto;" />

## Automated Traffic Violation Detection and Classification using Computer Vision

<img src="architecture.png" alt="System Architecture" width="120%" style="max-width: 150%; height: auto;" />

Gravelroad AI is an intelligent computer vision platform that is designed to automatically detect, classify, and document traffic violations from traffic images and videos. The system combines object detection, multi-object tracking, license plate recognition, evidence generation, and analytics to assist traffic authorities in monitoring traffic violations more efficiently.

The primary objective of the proposed system is to reduce the load on manual monitoring of the footage and provide an automated way of handling all the live feed and which is capable of processing large amount of traffic data while generating reliable and accurate evidence for traffic law enforcement to act upon.

---

# Features

The current prototype includes the following functions:

### Vehicle and Road User Detection

* Detection of cars, buses, trucks, motorcycles, bicycles, and pedestrians.
* Based on the YOLOv8 object detection framework.
* Generating bounding boxes and calculate confidence score accordingly.

### Multi-Object Tracking

* BoT-SORT based vehicle tracking.
* Constant vehicle identification across multiple frames of a live video feed.
* Tracking vehicle trajectory.

### Traffic Violation Detection

* Illegal Parking Detection.
* Helmet Non-Compliance Detection.
* Violation analysis on a rule by rule basis framework.

<img src="illegal parking.jpg" alt="Illegal Parking" width="60%" style="max-width: 60%; height: auto;" />

### License Plate Recognition

* Localization of vehicle number plates.
* OCR-based text extraction.
* Vehicle registration identification.

<img src="ocr result.jpg" alt="OCR Result" width="60%" style="max-width: 60%; height: auto;" />

### Evidence Generation

* Automatic generation of annotated violation images.
* Timestamp generation.
* Labeling violations.
* Confidence score being preserved.

### Violation Logging

* Vehicle ID recording.
* Violation type recording.
* Timestamp is stored.
* Evidence csv path is maintained.

### Analytics Dashboard

* Violation statistics.
* Violation distribution analysis.
* Violation records that can be searched.
* Historical data based on violation tracking.

---

# System Architecture

The architecture of Gravelroad AI consists of six major components:

* Input Sources
* AI Processing Engine
* Violation Detection Engine
* License Plate Recognition
* Evidence Generation
* Analytics and Reporting

Traffic images are first acquired from CCTV cameras, roadside surveillance systems, and traffic monitoring, then the  infrastructure is first processed by the AI Processing Engine. The processing engine then performs image enhancement, vehicle detection, object tracking, and road understanding.

The processed information is then forwarded to the Violation Detection Engine, where vehicle behavior is analyzed against predefined traffic rules (which is different for each road). Once a violation is detected, the Evidence Generation module produces evidence photos with annotations and markings containing bounding boxes, timestamps, confidence scores, and violation labels.

Detected vehicles are simultaneously forwarded to the License Plate Recognition module, where OCR techniques are used to extract vehicle registration information. The resulting violation records are stored in a centralized database and are later utilized by the Analytics and Reporting module for analyzing the data statistically (like Pie Chart and Bar Graph form).

---

# Technology Stack

### Computer Vision

* OpenCV
* YOLOv8

### Tracking

* BoT-SORT

### OCR

* EasyOCR

### Data Processing

* Pandas
* NumPy

### Dashboard made on

* Streamlit
* Plotly

### Programming Language

* Python

---

# Prototype Status

| Module                    | Status      |
| ------------------------- | ----------- |
| Vehicle Detection         | Completed   |
| Multi-Object Tracking     | Completed   |
| Illegal Parking Detection | Completed   |
| Helmet Detection          | Completed   |
| License Plate OCR         | Completed   |
| Evidence Generation       | Completed   |
| Violation Logging         | Completed   |
| Analytics Dashboard       | Completed   |
| Wrong Side Driving        | In Progress |
| Stop-Line Violation       | In Progress |

---

# Analytics Dashboard

The Analytics Dashboard converts raw violation records into outputs that can be easily understood and can hence, assist traffic authorities in monitoring traffic violations and identifying recurring patterns (Example: ID-213 had done Parking Violations more than three time).

The dashboard currently supports:

* Total violation statistics.
* Violation distribution visualization.

---

# Installation

### Clone Repository

```bash
git clone <repository-url>
cd traffic-flipkart-idea-3
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Detection Pipeline

```bash
python main.py
```

### Launch Analytics Dashboard

```bash
streamlit run backend/dashboard.py
```

---

# Future Scope

Future enhancements may include:

* Stop-Line Violation Detection.
* Red-Light Violation Detection.
* Triple Riding Detection.
* Seatbelt Non-Compliance Detection.
* Cloud-Based Deployment.
* Automated E-Challan Generation.
* Smart City Integration.
* Real-Time Traffic Monitoring.
* Vehicle Re-Identification Across Multiple Cameras.

---

# Team

**Team Name:** Oster

**Project:** Gravelroad AI

**Challenge:** Flipkart Gridlock Hackathon 2.0.
