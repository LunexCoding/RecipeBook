import shutil
from pathlib import Path


class FileSystem:

    def __init__(self, root):
        self._root = Path(root)

    def initTree(self, tree):
        for path in tree:
            path = self._root / path
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)

    def removeFile(self, path):
        Path(self._root / path).unlink()

    def removeTree(self, path=None):
        path = self._root / path if path is not None else self._root
        shutil.rmtree(path)

    def listDir(self):
        return list(self._root.iterdir())

    def destruction(self):
        self.removeTree()


# Module testing
if __name__ == "__main__":
    data = FileSystem('data')
    data.initTree(
        [
            'sources/files',
            'processing/files'
        ]
    )
    sourcesFiles = FileSystem('data/sources/files')
    sourcesFiles.initTree(
        [
            'doc'
            'pdf',
            'site/html/css'
        ]
    )
    processingFiles = FileSystem('data/processing/files')
    processingFiles.initTree(
        [
            'mainCSV',
            'pandasFrames'
        ]
    )

    with open('data/processing/files/mainCSV/test.txt', 'w') as file: pass
    processingFiles.removeFile('mainCSV/test.txt')
    processingFiles.removeTree('mainCSV')
    processingFiles.destruction()
    data.destruction()
