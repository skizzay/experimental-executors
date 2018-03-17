from conans import ConanFile, tools
import os


class ExperimentalexecutorsConan(ConanFile):
    name = "experimental-executors"
    version = "1.0.0"
    license = "MIT"
    url = "https://github.com/skizzay/experimental-executors"
    description = "Conan package for the executors c++ proposal"
    no_copy_source = True
    # No settings/options are necessary, this is header only

    def source(self):
        '''retrieval of the source code here. Remember you can also put the code in the folder and
        use exports instead of retrieving it with this source() method
        '''
        self.run("git clone git@github.com:executors/executors-impl.git")

    def package(self):
        self.copy("*", src=os.path.join("executors-impl", "include"), dst="include",
                keep_path=True)
