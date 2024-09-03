from pathlib import Path
from typing import Any
from mlPro.logger import logger

# Ensure get_size is defined here
def get_size(path: Path) -> str:
    """Returns the size of the file or directory."""
    size_in_bytes = sum(f.stat().st_size for f in path.glob('**/*') if f.is_file())
    return f"{size_in_bytes / (1024 * 1024):.2f} MB"

def read_yaml(path_to_yaml: Path) -> Any:
    logger.info(f"Reading YAML file from: {path_to_yaml}")
    # Your implementation here
    return {}

def create_directories(paths: list) -> None:
    for path in paths:
        Path(path).mkdir(parents=True, exist_ok=True)
        logger.info(f"Created directory at: {path}")
