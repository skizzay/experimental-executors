from conans import ConanFile, CMake
import os

class ExperimentalexecutorsTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def __init__(self, *args, **kwargs):
        super(ExperimentalexecutorsTestConan, self).__init__(*args, **kwargs)
        self._cmake = None

    def build(self):
        self._cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
        self._cmake.configure()
        self._cmake.build()

    def test(self):
        self._cmake.test()
