import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def setup_logging(log_file='app.log'):
    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)


def write_to_file(file_path, content):
    """
    Write content to a file.
    If the file does not exist, it will be created.
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create directories if they don't exist
    with open(file_path, 'w') as f:
        f.write(content)
    logging.info(f'Content written to {file_path}')