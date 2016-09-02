import unittest
import shutil
import os

import filesystem as fs


class fs_test(unittest.TestCase):
    FOLDER = './tmp'

    def create_file(self, name):
        with open(name, 'w') as f:
            f.write(name)

    def create_link(self, name):
        link = name + '_link'
        os.symlink(name, link)

    def setUp(self):
        if os.path.exists(fs_test.FOLDER):
            self.tearDown()

        os.mkdir(fs_test.FOLDER)
        names = ['a', 'b', 'c', 'd']
        self.files = [os.path.join(fs_test.FOLDER, f) for f in names]
        map(self.create_file, self.files)

        subfolder = os.path.join(fs_test.FOLDER, 'sub')
        os.mkdir(subfolder)
        self.subfiles = [os.path.join(subfolder, f) for f in names]
        map(self.create_file, self.subfiles)

    def tearDown(self):
        shutil.rmtree(fs_test.FOLDER)

    def test_find_files_default(self):
        result = fs.find_files(fs_test.FOLDER)
        self.assertEqual(self.files, result)

    def test_find_files_recursive(self):
        result = fs.find_files(fs_test.FOLDER, recursive=True)
        expected = self.subfiles + self.files
        self.assertEqual(expected.sort(), result.sort())

    def test_find_files_pattern(self):
        result = fs.find_files(fs_test.FOLDER, pattern='a')
        self.assertEqual(len(result), 1)

    def test_find_files_pattern_recursive(self):
        import pdb; pdb.set_trace()
        result = fs.find_files(fs_test.FOLDER, pattern='a', recursive=True)
        self.assertEqual(len(result), 2)


if __name__ == "__main__":
    unittest.main()
