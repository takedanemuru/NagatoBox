
import os
import shutil


def ensure(source_path, target_path):
    if os.path.exists(target_path):
        return
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    shutil.copy(source_path, target_path)
