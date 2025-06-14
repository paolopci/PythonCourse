import zipfile


def extract_zip(zip_path, dest_dir):
    """
    Extracts a zip file to a specified directory.

    :param zip_path: Path to the zip file.
    :param dest_dir: Directory where the contents will be extracted.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as archive:
            archive.extractall(dest_dir)
        print(f"Extraction complete: {zip_path} -> {dest_dir}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")


# if __name__ == "__main__":
#     extract_zip('./dest/compressed.zip', './aaa')
