import environ

env = environ.Env()
from pathlib import Path

import boto3

BASE_DIR = Path(__file__).resolve(strict=True)
env = environ.Env()
env.read_env(str(BASE_DIR / ".env"))
# Replace with your Supabase project credentials
access_key_id = env("DJANGO_AWS_ACCESS_KEY_ID",default="ae187701acd22a77779ce3ebfa32e101")  # type: ignore  # noqa: E501, PGH003
secret_access_key = env("DJANGO_AWS_SECRET_ACCESS_KEY",default="c92576a34dd08fbd5932efe0a32cf363f5a17c5af1da5ec4c390da815dab6962")  # type: ignore  # noqa: E501, PGH003
region = env("DJANGO_AWS_S3_REGION_NAME",default="us-east-2")  # type: ignore  # noqa: PGH003
endpoint_url = env("DJANGO_AWS_S3_CUSTOM_DOMAIN",default="https://fowvdrdkbqhmevigbkyb.supabase.co/storage/v1/s3")  # type: ignore  # noqa: PGH003
session_token = "rDmcvO1nYQnM3tnb3yR+qFFxyqWo3f+NBXV0OuuAITCpUaw7ujBzLdIadvuPJHRwwE/tc9zsRRmQT1+NtnzlMA=="  # noqa: E501, S105

# Create an S3 client
s3_client = boto3.client(
    "s3",
    region_name=region,
    endpoint_url=endpoint_url,
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    #  aws_session_token=session_token,
)

response = s3_client.list_objects_v2(Bucket="mystore")
for obj in response.get('Contents', []):
    print(obj['Key'])
