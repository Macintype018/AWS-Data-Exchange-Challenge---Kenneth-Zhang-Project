# AWS Data Exchange Challenge - Kenneth Zhang Project
Kenneth Zhang's AWS Data Exchange Project

## General Overview of Mobility Data/Reports
Due to the COVID-19 Pandemic, Mobility data and it's trends continue to shift and alter.
Using this data, we can identify change-points in mobility data in order to identify different time periods or instances
where mobility was increased in the population, in specific industries, or other areas.
Mobility data is often collected as a series of points with latitude and longitude collected at intervals by devices such as smartphones, 
shared micromobility vehicles, on-board vehicle computers, or app-based navigation systems.
Mobility data often has a temporal element, assigning time as well as location to each point. Depending on the device used to capture the data,
other characteristics, such as the speed of travel, or who is making the trip, can be connected to each individual latitude/longitude point.
Throughout this document, mobility data is often referred to as “geospatial trip data”, “trip data”, “geospatial mobility data”, “geospatial data”,and “bread-crumb”.

• GPS Trace/ Breadcrumb Trail - The product of recording information about a trip by using
a series of points with latitude and longitude collected at regular intervals by devices such as
smartphones, bicycles, scooters, navigation systems, and vehicles. When mapped, a breadcrumb
trail can show the path of travel of an individual and/or vehicle. GPS trace data may or may not
have temporal data associated with each point.

• Individual Trip Records - For shared micromobility, ride-hail trips, and trips recorded in appbased
navigation systems, a GPS trace record is created for each unique trip. This record typically
includes start/end locations and times, route, and may include information tying that trip to a
specific user account. Individual trip records are sometimes referred to colloquially as “raw” or
“unprocessed” data. “Anonymized” trip data is that which has individual identifiers removed.

• Location Telemetry data - Any data that records the movements and sensor readings from a
vehicle including location, direction, speed, brake/throttle position, etc. Fleet operators may
use vehicle telemetry data to determine instances of dangerous driving such as harsh-braking
or excessive speeding. Some shared micromobility providers report that they can use scooter
telemetry data to determine if a scooter has been left in an upright vs tipped over position.

• Data Protection - Mechanisms for guarding against unauthorized access, including practices for
preventing unauthorized entities from accessing data. Also includes methods for diminishing the
usefulness of stolen data should a system be breached.

• Verifiable Data Audit - Tools or practices that automatically and routinely capture, log, and
report activity in a data set in order to ensure those accessing sensitive datasets are acting in an
approved manner.


## Using the FBProphet for Change-point Detection in Google Mobility Data/Reports of Different Countries
In this project, we will use mobility data provided by Google Inc.
We specifically chose the United Arab Emirates (UAE) for change-point detection and analysis as it was a country that had one of the least amounts of missing values in 
each of the recorded data columns. Although the FBProphet is robust against missing datapoints and positions, it is beneficial to have as many actual recorded data points.
