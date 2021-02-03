import numpy as np

from . import datasets, translation, deeptrack_wrapper


class PyAPI:
    def __init__(self):

        self.active_dataset = None

    # ==============================================
    # Utils
    # ==============================================
    def _assert_active_dataset(self):
        assert self.active_dataset is not None, "Active dataset not yet set."

    # ==============================================
    # API
    # ==============================================

    # DATASET
    def set_active_dataset(self, files, axis):
        self.active_dataset = datasets.parse_data_config(files=files, axis=axis)

    def get_next_from_active_dataset(self):
        self._assert_active_dataset()
        return translation.format_data_as_image(self.active_dataset.update().resolve())

    def get_data_by_path_from_active_dataset(self, path):
        self._assert_active_dataset()
        image = translation.format_data_as_image(
            self.active_dataset.update(path=path).resolve()
        )
        return image

    # FEATURES
    def get_available_features(self):
        return deeptrack_wrapper.get_all_features_for_frontend()
