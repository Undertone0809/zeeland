import json
import os

from zeeland import get_default_storage_path


def main():
    storage_path = get_default_storage_path("test")
    metadata_path = os.path.join(storage_path, "metadata.json")

    metadata = {"name": "test", "version": "1.0.0", "description": "Test metadata file"}

    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)

    print(f"Created metadata file at: {metadata_path}")
    with open(metadata_path, "r") as f:
        print("Content:")
        print(json.dumps(json.load(f), indent=4))


if __name__ == "__main__":
    main()
