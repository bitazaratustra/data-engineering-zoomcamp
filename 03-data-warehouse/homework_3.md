Homework 3

1 -840402
SELECT COUNT(*)
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022`;


2 - 18.82 for external / 47.60 MB for the Materialized Table

-- Para la tabla externa
SELECT COUNT(DISTINCT PULocationID)
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022_external`;

-- Para la tabla materializada
SELECT COUNT(DISTINCT PULocationID)
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022`;


3 - 1622
SELECT COUNT(*)
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022_external`
WHERE fare_amount=0;


4 - 	•	Partition by lpep_pickup_datetime Cluster on PUlocationID


5 - 	•	10.31 MB for non-partitioned table and 10.31 MB for the partitioned table
SELECT DISTINCT PULocationID
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022_external`
WHERE lpep_pickup_datetime BETWEEN TIMESTAMP('2022-06-01') AND TIMESTAMP('2022-06-30');


SELECT DISTINCT PULocationID
FROM `dtc-de-course-412514.DataEngCourseDataBase.green_taxi_trip_records_2022_partirioned`
WHERE lpep_pickup_datetime BETWEEN TIMESTAMP('2022-06-01') AND TIMESTAMP('2022-06-30');

6 - 	GCP Bucket

7 - False
