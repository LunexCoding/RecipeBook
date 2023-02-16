from pathlib import Path
from Logger import Logger


FILENAME = "log.md"
DIR = Path("logs")


logger = Logger()
logger.createLog(DIR, FILENAME)
with open(Path(DIR / FILENAME), "w") as file:
    file.write('```python\n')
