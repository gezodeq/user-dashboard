# utils.py
import logging
import os
import re
import json
from datetime import datetime
from uuid import uuid4

def generate_uuid():
    """Generate a random UUID."""
    return str(uuid4())

def generate_timestamp():
    """Generate a timestamp."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def extract_id_from_url(url: str) -> str:
    """Extract the ID from a URL."""
    match = re.search(r"/(\w+)", url)
    return match.group(1) if match else None

def load_json_file(file_path: str) -> dict:
    """Load a JSON file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} not found.")
    with open(file_path, "r") as file:
        return json.load(file)

def save_json_file(file_path: str, data: dict) -> None:
    """Save a JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def configure_logging(level: int = logging.INFO) -> None:
    """Configure logging."""
    logging.basicConfig(level=level)