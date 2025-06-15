import zipfile
import pathlib


def make_archive(filepaths, destination_folder):
    dest_path = pathlib.Path(destination_folder, 'compressed.zip')
    with zipfile.ZipFile(dest_path, "w") as zipf:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zipf.write(filepath, arcname=filepath.name)


# Example usage
if __name__ == "__main__":
    make_archive(filepaths=['bonus5.py',
                 'Bonus4.py'], destination_folder='dest')
