import unittest
from pathlib import Path
from helpers.fileSystem import FileSystem
from helpers.fileSystemExceptions import (
    IsNotEmptyException,
    PathExistsException,
    PathExistsAsFileException,
    PathExistsAsDirectoryException,
    PathNotFoundException,
    IsNotDirectoryException
)
from helpers.customException import TypeException


_FIXTURES_DIRECTORY = Path("fixtures")


class TestFileSystem(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._fileSystem = FileSystem()
        cls._fileSystem.makeDir(_FIXTURES_DIRECTORY)
        cls._data = {"key": "value"}

    @classmethod
    def tearDownClass(cls):
        cls._fileSystem.removeTree(_FIXTURES_DIRECTORY)

    def test_create(self):
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.create(_FIXTURES_DIRECTORY)
        with self.assertRaises(TypeException):
            self._fileSystem.create(_FIXTURES_DIRECTORY / "fixturesTest.txt", wipe=5)
        self.assertTrue(self._fileSystem.create(_FIXTURES_DIRECTORY / "fixturesTest.txt"))
        self._fileSystem.writeText(_FIXTURES_DIRECTORY / "fixturesTest.txt", str(self._data))  # нужно ли мне это проверять
        self.assertTrue(self._fileSystem.create(_FIXTURES_DIRECTORY / "fixturesTest.txt", wipe=True))
        self.assertTrue(self._fileSystem.create(_FIXTURES_DIRECTORY / "fixturesTesting.txt", wipe=True))
        self.assertTrue(len(self._fileSystem.readText(_FIXTURES_DIRECTORY / "fixturesTest.txt")) == 0)

    def test_getFilename(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.getFilename(_FIXTURES_DIRECTORY / "fsgdfg")
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.create(_FIXTURES_DIRECTORY)
        self.assertEqual(self._fileSystem.getFilename(_FIXTURES_DIRECTORY / "fixturesTest.txt"), "fixturesTest")
        self.assertEqual(self._fileSystem.getFilename(_FIXTURES_DIRECTORY / "fixturesTest.txt", True), "fixturesTest.txt")

    def test_exists(self):
        self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "fixturesTest")
        self.assertTrue(self._fileSystem.exists(_FIXTURES_DIRECTORY / "fixturesTest.txt"))
        self.assertTrue(self._fileSystem.exists(_FIXTURES_DIRECTORY / "fixturesTest"))

    def test_isDir(self):
        self._fileSystem.isDir(_FIXTURES_DIRECTORY / "fixturesTest.txt")
        self._fileSystem.create(_FIXTURES_DIRECTORY / "fixturesTest.txt")
        self.assertTrue(self._fileSystem.isDir(_FIXTURES_DIRECTORY / "fixturesTest"))

    def test_isEmpty(self):
        with self.assertRaises(IsNotDirectoryException):
            self._fileSystem.isEmpty(_FIXTURES_DIRECTORY / "fixturesTest.txt")
        with self.assertRaises(IsNotEmptyException):
            self._fileSystem.isEmpty(_FIXTURES_DIRECTORY)
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.isEmpty("terddfg")
        self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "testEmpty")
        self.assertTrue(self._fileSystem.isEmpty(_FIXTURES_DIRECTORY / "testEmpty"))

    def test_isFile(self):
        self.assertTrue(self._fileSystem.isFile(_FIXTURES_DIRECTORY / "fixturesTest.txt"))
        self.assertFalse(self._fileSystem.isFile(_FIXTURES_DIRECTORY))

    def test_makeDir(self):
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "fixturesTest.txt")
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "fixturesTest.txt", recreate=True)
        with self.assertRaises(PathExistsException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY)
        self.assertTrue(self._fileSystem.makeDir(_FIXTURES_DIRECTORY, recreate=True))
        self.assertTrue(self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "testing"))

    def test_makeDirs(self):
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "fixturesTest.txt")
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY / "fixturesTest.txt", recreate=True)
        with self.assertRaises(PathExistsException):
            self._fileSystem.makeDir(_FIXTURES_DIRECTORY)
        self.assertTrue(self._fileSystem.makeDirs(_FIXTURES_DIRECTORY / "testing", recreate=True))
        self.assertTrue(self._fileSystem.makeDirs(_FIXTURES_DIRECTORY / "testing" / "testingDeep"))

    def test_remove(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.remove(_FIXTURES_DIRECTORY / "rgfdgdf")
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.remove(_FIXTURES_DIRECTORY)
        self.assertTrue(self._fileSystem.remove(_FIXTURES_DIRECTORY / "fixturesTest.txt"))

    def test_removeDir(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.removeDir(_FIXTURES_DIRECTORY / "testing505")
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.removeDir(_FIXTURES_DIRECTORY / "fixturesTesting.txt")
        with self.assertRaises(IsNotEmptyException):
            self._fileSystem.removeDir(_FIXTURES_DIRECTORY)
        self.assertTrue(self._fileSystem.removeDir(_FIXTURES_DIRECTORY / "testing" / "testingDeep"))

    def test_removeTree(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.removeTree(_FIXTURES_DIRECTORY / "testDelTree")
        with self.assertRaises(PathExistsAsFileException):
            self._fileSystem.removeTree(_FIXTURES_DIRECTORY / "fixturesTesting.txt")
        self.assertTrue(self._fileSystem.removeTree(_FIXTURES_DIRECTORY / "testing"))

    def test_readJson(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.readJson(_FIXTURES_DIRECTORY / "readingJson")
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.readJson(_FIXTURES_DIRECTORY)
        self._fileSystem.writeJson(_FIXTURES_DIRECTORY / "fixturesTest.txt", self._data)
        self.assertTrue(len(self._fileSystem.readJson(_FIXTURES_DIRECTORY / "fixturesTest.txt")) != 0)

    def test_readText(self):
        with self.assertRaises(PathNotFoundException):
            self._fileSystem.readJson(_FIXTURES_DIRECTORY / "readingJson")
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.readJson(_FIXTURES_DIRECTORY)
        self.assertTrue(len(self._fileSystem.readText(_FIXTURES_DIRECTORY / "fixturesTest.txt")) != 0)

    def test_writeJson(self):
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.writeJson(_FIXTURES_DIRECTORY, self._data)
        self._fileSystem.writeJson(_FIXTURES_DIRECTORY / "fixturesTest.txt1", "gfghfgh")
        self.assertTrue(self._fileSystem.writeJson(_FIXTURES_DIRECTORY / "fixturesTest.txt", self._data))


    def test_writeText(self):
        with self.assertRaises(PathExistsAsDirectoryException):
            self._fileSystem.writeText(_FIXTURES_DIRECTORY, str(self._data))
        with self.assertRaises(TypeException):
            self._fileSystem.writeText(_FIXTURES_DIRECTORY / "fixturesTest.txt", self._data)
        self.assertTrue(self._fileSystem.writeText(_FIXTURES_DIRECTORY / "fixturesTest.txt", str(self._data)))


if __name__ == '__main__':
    unittest.main()
