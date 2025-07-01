# AXA Data Challenge: CitiBike & NYPD Crash Datasets Analysis
This repository contains analysis of **bike-sharing usage patterns**, **cyclist accident trends**, and offers **risk analysis** that can drive **partnership opportunities between CitiBike and insurance companies**.

## Part 1: CitiBike Data Analysis
- Analyzed user types: **members vs. casuals** (trip share, distance, duration)
- Breakdown of **bike types** (classic vs. electric) and preference by user type
- Explored **trip volumes** by day of week, hour, month and season
- Investigated **ride duration and distance patterns**
- Conducted **geospatial analysis**: Top start & end stations and Most frequent routes

## Part 2: NYPD Bicycle Accident Analysis
- Assessed **accident volume** by day of week, hour, month and season
- Analyzed **accident severity** (injuries and fatalities)
- Identified **top contributing factors**

## Part 3: Combined Risk Analysis
- High-risk station detection
- Time-based risk patterns
- Route risk scoring

## Part 4: Machine Learning Analysis
- Created a **binary risk label** (risky vs. safe) using accident proximity
- Built classification models using:
  - Features: ride hour, ride day of the week, ride duration, ride distance, etc.
  - Outcome: whether a trip is **"risky"**
- Balanced data, trained model, and evaluated performance

## Tools & Technologies Used

- Python (Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn, Folium)
- Geospatial analysis (BallTree + Haversine distance)
- Machine learning (Logistic Regression, Random Forest)
- Jupyter Notebooks
