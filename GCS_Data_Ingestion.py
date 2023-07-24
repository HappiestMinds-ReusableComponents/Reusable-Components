# Imports the Google Cloud client library
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=r"C:\Users\Sidharth.chhotaray\Downloads\service_key.json"

from google.cloud import storage
import sys

# Instantiates a client
storage_client = storage.Client()

# total arguments
n = len(sys.argv)
#print("Total arguments passed:", n)
 
# Arguments passed
print("\nName of Python script:", sys.argv[0])

if n < 4:
    print("Total arguments passed:", n , "expected 4 parameters")
    print("===========exiting the the script parameters are not defined propoerly============")
    print("\n\n1st parameter should be GCP Bucket name without gs://")
    print("\n2nd parameter should be Target GCP Bucket name along with filename without gs://")
    print("\n3rd parameter should be Local file names and path thats needs to be uploaded")
    print("\n\n===========exiting the the script parameters are not defined propoerly============")
    #python test.py "happiest_health_bucket" "APItest/epfo.pdf" "C:\Users\Sidharth.chhotaray\Downloads\epfo.pdf"
    exit(1)
else:
    print("Total arguments passed:", n , " which is correct")


# specify your bucket name
bucket = storage_client.get_bucket(sys.argv[1]) 

# specify your target bucket and file name in GCS storage
blob = bucket.blob(sys.argv[2])
blob.upload_from_filename(sys.argv[3])

print("===========Success Msg============")
print("\n\nData Ingestion of \""+ sys.argv[3] + "\" on to GCS bucket \"" +sys.argv[1]+"/"+sys.argv[2]+"\" is completed\n\n")
print("===========Success Msg============")