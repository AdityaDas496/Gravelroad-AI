# 🛣️ Gravelroad AI 🛣️

## Introduction

Traffic surveillance systems generate large volumes of traffic images every day. Manual inspection of these images is quite time consuming, labor intensive and also prone to inconsistencies. This project proposes, Gravelroad AI, which is an intelligent computer vision platform capable of automatically detecting vehicles, identifying traffic violations, extracting vehicle information, and generating evidence against road laws for traffic law enforcement.

---

## Proposed Approach

The proposed solution, Gravelroad AI, is a computer-vision based traffic analysis platform that is designed to automatically identify, classify, and document various traffic violations from traffic photographs and surveillance imagery. The system’s main aim is to reduce dependency on manual monitoring by providing an intelligent and scalable framework that is capable of processing large volumes of traffic data efficiently.

The workflow begins with the acquisition of traffic images from multiple sources, which include CCTV cameras, roadside surveillance systems, traffic monitoring infrastructure, and photographic evidence.

The images are first passed through an image preprocessing stage where quality enhancement techniques are used, such as:

* Contrast Enhancement (CLAHE)
* Noise Removal
* Brightness Correction
* Shadow Handling

These techniques are applied to improve detection performance under various environmental conditions.

Once the images are enhanced, they are then processed by a vehicle and road-user detection system which is based on modern deep learning object detection models such as YOLOv8.

This system identifies and localizes different traffic participants, which includes:

* Cars
* Buses
* Trucks
* Motorcycles
* Bicycles
* Pedestrians

For video-based surveillance scenarios, a multi-object tracking system can further assign unique identities which will be able to detect vehicles and maintain their trajectories across consecutive frames.

To provide a contextual understanding of the traffic environment, the system also incorporates a road understanding component. This module defines:

* Lane Regions
* Parking Zones
* Road Boundaries
* Stop Lines
* Traffic Signal Regions

These enable violation-specific rule evaluation. By combining object detection results with road context information, the system can accurately determine whether a vehicle violates traffic regulation.

The violation detection engine serves as core decision-making component of the platform. It analyzes detected vehicles and road users and identifies multiple categories of traffic violations, ranging from:

* Helmet Non-Compliance
* Seatbelt Non-Compliance
* Triple Riding
* Wrong-Side Driving
* Stop-Line Violations
* Illegal Parking

Each and every detected violation is assigned a confidence score which indicates the reliability of the prediction and is categorized to predefined violation classes for further processing.

For vehicle identification, the system incorporates a License Plate Recognition (LPR) system. This module first detects the vehicle’s number plate and then subsequently applies Optical Character Recognition (OCR) techniques to extract the vehicle registration number from the image.

The extracted registration information is then linked to the corresponding violation record which enables efficient vehicle identification and enforcement actions.

In order to support traffic enforcement and auditing, the platform includes evidence generating module that automatically produces annotated images highlighting detected violations.

Each evidence record contains:

* Bounding Boxes
* Violation Labels
* Timestamps
* Confidence Scores
* Vehicle Registration Information

This ensures transparency and provides reliable and convenient evidence for traffic authorities.

All violation records are stored in a centralized violation database which enables efficient storage retrieval, and management of historical data.

An analytics and reporting module utilizes these records and generates:

* Violation Statistics
* Trend Analyses
* Searchable Reports
* Enforcement Summaries

These help assist traffic authorities in decision-making and resource allocation.

---

## System Architecture

The architecture of Gravelroad AI consists of six major components:

1. Input Sources
2. AI Processing Engine
3. Violation Detection Engine
4. License Plate Recognition
5. Evidence Generation
6. Analytics and Reporting

### Architecture Diagram

<img src="architecture.png" alt="System Architecture" width="100%" style="max-width: 150%; height: auto;" />

Traffic images acquired from surveillance infrastructure are first processed by the AI Processing Engine, which performs:

* Preprocessing
* Object Detection
* Multi-Object Tracking
* Road Understanding

The processed information is then forwarded to the Violation Detection Engine, where the traffic violation is identified and classified.

Simultaneously, detected vehicles are passed to the License Plate Recognition module for vehicle identification.

Violation records and supporting evidence are stored in the centralized database, which serves as foundation for analytics, reporting and performance evaluation.

---

## Assumptions

The proposed solution is developed under the following assumptions:

1. Traffic images and surveillance footage are of sufficient quality for object detection and analysis.
2. Vehicles and road users are reasonably visible and are not permanently occluded.
3. Traffic signs, road boundaries, lane markings, stop lines, and parking regions are either visible or can be defined using region-based rules.
4. Vehicle number plates are visible in at least a subset of captured images for OCR-based extraction.
5. Environmental factors such as rain, fog, low light, and shadows may affect detection accuracy but can be partially mitigated through preprocessing techniques.
6. The system is intended to assist traffic authorities and not replace human verification in critical enforcement decisions.

---

## Expected Evaluation Strategy

The effectiveness of Gravelroad AI will be evaluated using both detection and system level performance metrics.

### Detection and Classification Metrics

| Metric    | Purpose                                     |
| --------- | ------------------------------------------- |
| Accuracy  | Overall correctness of predictions          |
| Precision | Reduction of false positives                |
| Recall    | Reduction of false negatives                |
| F1-Score  | Balanced evaluation of precision and recall |
| mAP       | Object detection performance                |

These metrics assess the system’s ability to correctly identify vehicles, road users, and traffic violations while minimizing false positives and false negatives.

### License Plate Recognition Metrics

The License Plate Recognition module will be evaluated using:

* OCR Accuracy
* Character-Level Recognition Rate

### Evidence Generation Evaluation

Evidence generation will be assessed and verified based on:

* Correctness of Annotations
* Timestamp Accuracy
* Metadata Consistency
* Violation Classification Accuracy

### System Performance Metrics

Computational efficiency will be measured using:

* Inference Time
* Processing Throughput
* Frames Per Second (FPS)

Scalability will be evaluated by analyzing the system's performance under increasing traffic density and larger image datasets.

---

## Expected Outcomes

The proposed system is expected to automatically identify, classify and document multiple traffic violations from photographic evidence with minimal human intervention.

The platform’s aim is to reduce manual effort and improve consistency in traffic monitoring and provide with real time evidence for law enforcement by combining:

* Computer Vision
* Object Detection
* Tracking
* OCR
* Analytics

The system generates:

* Annotated Violation Records
* Vehicle Registration Information
* Searchable Violation Databases
* Statistical Insights

These capabilities can support traffic management authorities in making informed decisions.

---

## Future Scope

Future enhancements may include:

* Cloud-Based Deployment for Large-Scale City-Wide Monitoring
* Integration with Smart Traffic Infrastructure
* Automatic Challan Generation
* Real-Time Alert Systems
* Advanced Vehicle Re-Identification
* AI-Assisted Traffic Congestion Analysis

Additional violation categories and improved deep learning models can also be integrated to further increase the system’s accuracy and adaptability.
