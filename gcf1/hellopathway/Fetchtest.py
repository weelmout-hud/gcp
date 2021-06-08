from google.cloud import storage
import os
os.environ.setdefault("GCLOUD_PROJECT", "even-kite-315518")

client = storage.Client()
bucket = storage.Bucket(client, "hcl_storage", user_project="even-kite-315518")
all_blobs = list(client.list_blobs(bucket))
print(all_blobs)