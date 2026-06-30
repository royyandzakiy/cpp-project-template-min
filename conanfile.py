from conan import ConanFile

class MyProjectConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeConfigDeps"

    def requirements(self):
        self.requires("fmt/12.1.0")