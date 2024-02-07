Homework  1

	0.	—rm
	0.	0.36.2

	0.	15612
	0.

SELECT
    CAST(lpep_pickup_datetime AS DATE) AS pickup_date,
    MAX(trip_distance) AS max_trip_distance
FROM
    green_taxi_data
WHERE
    CAST(lpep_pickup_datetime AS DATE) IN ('2019-09-18', '2019-09-16', '2019-09-26', '2019-09-21')
GROUP BY
    pickup_date
HAVING
    MAX(trip_distance) IS NOT NULL;



	0.	Brookling, Manhattan, Queens



SELECT
    zpu."Borough",
    SUM(g."total_amount") AS "total_amount_sum"
FROM
    green_taxi_data g
JOIN
    zones zpu ON g."PULocationID" = zpu."LocationID"
WHERE
    CAST(lpep_pickup_datetime AS DATE) = '2019-09-18'
    AND zpu."Borough" != 'Unknown'
GROUP BY
    zpu."Borough"
HAVING
    SUM(g."total_amount") > 50000
ORDER BY
    "total_amount_sum" DESC
LIMIT 3;



	0.	JFK Airport


WITH AstoriaPickups AS (
    SELECT
        g.*,
        zdo."Zone" AS dropoff_zone_name
    FROM
        green_taxi_data g
    JOIN
        zones zpu ON g."PULocationID" = zpu."LocationID"
    JOIN
        zones zdo ON g."DOLocationID" = zdo."LocationID"
    WHERE
        CAST(g.lpep_pickup_datetime AS DATE) >= '2019-09-01'
        AND CAST(g.lpep_pickup_datetime AS DATE) <= '2019-09-30'
        AND zpu."Zone" = 'Astoria'
)
SELECT
    dropoff_zone_name,
    MAX(tip_amount) AS max_tip_amount
FROM
    AstoriaPickups
GROUP BY
    dropoff_zone_name
ORDER BY
    max_tip_amount DESC
LIMIT 1;



7)
➜  terraform_basic git:(bitazaratustra) ✗ terraform apply

Terraform used the selected providers to generate the following execution plan.
Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.dataset will be created
  + resource "google_bigquery_dataset" "dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "DataEngCourseDataBase"
      + delete_contents_on_destroy = false
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + labels                     = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + project                    = "dtc-de-course-412514"
      + self_link                  = (known after apply)
    }

  # google_storage_bucket.data-lake-bucket will be created
  + resource "google_storage_bucket" "data-lake-bucket" {
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "dtc-de-course-412514-terra-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + uniform_bucket_level_access = true
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "Delete"
            }
          + condition {
              + age                   = 30
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }

      + versioning {
          + enabled = true
        }
    }

Plan: 2 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

google_bigquery_dataset.dataset: Creating...
google_storage_bucket.data-lake-bucket: Creating...
google_bigquery_dataset.dataset: Creation complete after 2s [id=projects/dtc-de-course-412514/datasets/DataEngCourseDataBase]
google_storage_bucket.data-lake-bucket: Creation complete after 2s [id=dtc-de-course-412514-terra-bucket]
