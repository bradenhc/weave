########################################################################################
## Copyright 2023 Braden Hitchcock - MIT License  https://opensource.org/licenses/MIT ##
########################################################################################
from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout


class ConanProject(ConanFile):
    name = "hc_project"
    version = "0.1.0"

    description = "<Description of Project here>"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    license = "<Put the package license here>"

    topics = "cpp"

    settings = "os", "compiler", "build_type", "arch"

    options = {
        "coverage": [True, False],
        "fPIC": [True, False],
        "shared": [True, False],
    }

    default_options = {"coverage": True, "fPIC": True, "shared": False}

    exports_sources = (
        "CMakeLists.txt",
        "src/*",
        "include/*",
        "test/*",
        "docs/*",
        "LICENSE",
        "README.md",
    )

    def configure(self):
        if self.conf.get("user.build:coverage"):
            self.options.coverage = True

    def build_requirements(self):
        self.test_requires("gtest/1.13.0")

    def requirements(self):
        pass

    def layout(self):
        cmake_layout(self)

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.variables["CONAN_PKG_NAME"] = self.name
        tc.variables["CONAN_PKG_VERSION"] = self.version
        tc.variables["HC_DISABLE_TESTS"] = self.conf.get("tools.build:skip_test", False)
        tc.variables["HC_SHARED"] = self.options.shared
        if self.options.coverage:
            tc.variables["HC_ENABLE_COVERAGE"] = True
            tc.variables["HC_DISABLE_COMPONENT_TESTS"] = True
        elif self.conf.get("user.build:skip_component_test"):
            tc.variables["HC_DISABLE_COMPONENT_TESTS"] = True
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["hc_project"]
