from django.test import TestCase

from .. import storage


class StorageTestCase(TestCase):
    def test_photo_file(self):
        with self.settings(STORAGES={"photo": {"driver": "file"}}):
            self.assertIsInstance(storage.get_storage_class(), storage.PhotoStorageFile)

    def test_photo_s3(self):
        with self.settings(STORAGES={"photo": {"driver": "s3"}}):
            self.assertIsInstance(storage.get_storage_class(), storage.PhotoStorageS3)

    def test_photo_azure(self):
        with self.settings(STORAGES={"photo": {"driver": "azure"}}):
            self.assertIsInstance(
                storage.get_storage_class(), storage.PhotoStorageAzure
            )
