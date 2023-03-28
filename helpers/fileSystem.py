import os
from pathlib import Path
from .jsonTools import JsonTools
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)
from helpers.customException import TypeException


class FileSystem:
    def __init__(self):
        pass

    def create(self, path, wipe=False):
        path = Path(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        if not isinstance(wipe, bool):
            raise TypeException("wipe", type(wipe).__name__, bool.__name__)
        path.open(mode="a").close()
        if wipe is True:
            os.truncate(str(path), 0)
        return True

    def getFilename(self, path, suffix=False):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        return path.stem if suffix is False else path.name

    def getSortedDir(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        return sorted(path.glob("*.json"))

    def isFile(self, path):
        return Path(path).is_file()

    def isDir(self, path):
        return Path(path).is_dir()

    def isEmpty(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if not path.is_dir():
            raise IsNotDirectoryException(path)
        if not len(os.listdir(path)) == 0:
            raise IsNotEmptyException(path)
        return True

    def makeDir(self, path, recreate=False):
        path = Path(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if (path.exists() and recreate is False):
            raise PathExistsException(path)
        path.mkdir(exist_ok=recreate)
        return True

    def makeDirs(self, path, recreate=False):
        path = Path(path)
        if (path.exists() and Path(path).is_file()):
            raise PathExistsAsFileException(path)
        if (path.exists() and recreate is False):
            raise PathExistsException(path)
        path.mkdir(parents=True, exist_ok=recreate)
        return True

    def remove(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        path.unlink()
        return True

    def removeDir(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        if not self.isEmpty(path):
            raise IsNotEmptyException(path)
        path.rmdir()
        return True

    def removeTree(self, path):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_file()):
            raise PathExistsAsFileException(path)
        for child in path.glob("*"):
            if child.is_file():
                child.unlink()
            else:
                self.removeTree(child)
        path.rmdir()
        return True

    def exists(self, path):
        return Path(path).exists()

    def readJson(self, path, encoding="utf-8"):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        with path.open(encoding=encoding) as file:
            return JsonTools.jsonLoad(file)

    def readText(self, path, encoding="utf-8"):
        path = Path(path)
        if not path.exists():
            raise PathNotFoundException(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        with path.open("r", encoding=encoding) as file:
            return file.read()

    def writeJson(self, path, contents, encoding="utf-8"):
        path = Path(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        try:
            with path.open("w", encoding=encoding) as file:
                JsonTools.jsonWrite(contents, file)
                return True
        except:
            raise TypeException("contents", type(contents).__name__, "Recipe")

    def writeText(self, path, contents, encoding="utf-8"):
        path = Path(path)
        if (path.exists() and path.is_dir()):
            raise PathExistsAsDirectoryException(path)
        if not isinstance(contents, str):
            raise TypeException("contents", type(contents).__name__, str.__name__)
        with path.open("w", encoding=encoding) as file:
            file.write(contents)
        return True


fileSystem = FileSystem()
