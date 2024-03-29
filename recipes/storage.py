# Copyright 2022 Aleksandr Soloshenko
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf import settings
from django.core.files.storage import FileSystemStorage, Storage
from storages.backends.azure_storage import AzureStorage
from storages.backends.s3boto3 import S3Boto3Storage


class PhotoStorageFile(FileSystemStorage):
    pass


class PhotoStorageAzure(AzureStorage):
    location = settings.STORAGES["photo"]["location"]
    expiration_secs = None


class PhotoStorageS3(S3Boto3Storage):
    location = settings.STORAGES["photo"]["location"]
    querystring_auth = False


DRIVERS = {
    "s3": PhotoStorageS3,
    "azure": PhotoStorageAzure,
    "file": PhotoStorageFile,
}


def get_storage_class() -> Storage:
    photoStorageDriver = settings.STORAGES["photo"]["driver"]

    if photoStorageDriver not in DRIVERS:
        raise ValueError(f"Unknown storage driver: {photoStorageDriver}")

    photoStorage = DRIVERS[photoStorageDriver]()

    return photoStorage
