import requests
from google.cloud import storage

def upload_to_gcs(bucket_name, object_name, local_file):
    """
    Sube un archivo local a Google Cloud Storage.
    """
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)

def web_to_gcs(year, service, bucket_name):
    """
    Descarga archivos Parquet desde el web y los carga en Google Cloud Storage.
    """
    for i in range(1, 13):
        month = str(i).zfill(2)
        file_name = f"{service}_tripdata_{year}-{month}.parquet"

        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{file_name}"

        r = requests.get(url)

        if r.status_code == 200:
            with open(file_name, 'wb') as f:
                f.write(r.content)
            upload_to_gcs(bucket_name, f"{service}/{file_name}", file_name)
            print(f"Archivo {file_name} cargado correctamente en GCS.")
        else:
            print(f"Error al descargar {file_name}: {r.status_code}")

bucket_name = "ny_green_taxi_bucket"  # Reemplaza con el nombre de tu bucket en Google Cloud Storage
web_to_gcs('2022', 'green', bucket_name)
