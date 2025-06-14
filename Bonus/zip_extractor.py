import zipfile


def extract_zip(zip_path, extract_to):
    """
    Extracts a zip file to a specified directory.

    :param zip_path: Path to the zip file.
    :param extract_to: Directory where the contents will be extracted.
    """
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"Extraction complete: {zip_path} -> {extract_to}")
    except zipfile.BadZipFile:
        print(f"Error: {zip_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")
