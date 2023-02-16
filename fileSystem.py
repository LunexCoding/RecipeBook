import shutil
from pathlib import Path


class FileSystem:

    def __init__(self):
        self._root = None

    def createRoot(self, root):
        self._root = root
        Path(self._root).mkdir(parents=True, exist_ok=True)

    def initTree(self, tree):
        for path in tree:
            path = self._root / path
            if not path.exists():
                path.mkdir(parents=True, exist_ok=True)

    def removeFile(self, path):
        if self._root is not None:
            Path(self._root / path).unlink()
        else:
            Path(path).unlink()

    def removeTree(self, path=None):
        if self._root is not None:
            path = self._root / path if path is not None else self._root
        shutil.rmtree(path)

    def listDir(self):
        return list(self._root.iterdir())

    def destruction(self):
        self.removeTree()
