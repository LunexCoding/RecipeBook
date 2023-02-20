import shutil
from pathlib import Path


class FileSystem:

    def __init__(self):
        self._root = None

    def createRoot(self, root):
        self._root = root
        Path(self._root).mkdir(parents=True, exist_ok=True)

    def initTree(self, tree):
        if self._root is not None:
            for path in tree:
                path = self._root / path
                if not path.exists():
                    path.mkdir(parents=True, exist_ok=True)
        else:
            for path in tree:
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

    def listDir(self, path=None):
        if self._root is not None:
            return [file for file in self._root.glob('**/*') if file.is_file()]
        else:
            return [file for file in Path(path).glob('**/*') if file.is_file()]

    def getFileNameWithSuffix(self, listPaths):
        return [file.name for file in listPaths]

    def destruction(self):
        self.removeTree()
