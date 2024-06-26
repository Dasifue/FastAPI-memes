"File for minio configuration"

import os

from dotenv import load_dotenv


load_dotenv()

MINIO_HOSTNAME = os.getenv("MINIO_HOST")
MINIO_PORT = os.getenv("MINIO_PORT")
MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY")
MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY")
