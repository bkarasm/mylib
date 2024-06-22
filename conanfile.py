from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout
from conan.tools.files import update_conandata
from conan.tools.scm import Git
import os

required_conan_version = ">=1.53.0"

class MyLibConan(ConanFile):
    name = "mylib"
    url = "https://github.com/bkarasm/mylib"
    settings = "os", "compiler", "arch", "build_type"
    options = {
        "fPIC": [True, False],
    }
    default_options = {
        "fPIC": True,
    }

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def export(self):
        git = Git(self, self.recipe_folder)
        scm_commit = git.get_commit()
        update_conandata(self, {
            "sources": {
                "commit": scm_commit
                }
            }
        )

    def layout(self):
        return cmake_layout(self, src_folder="mylib")

    def source(self):
        git = Git(self)
        git.clone(url="git@github.com:bkarasm/mylib.git", target=".")
        git.checkout(commit=self.conan_data["sources"]["commit"])

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = [ "mylib" ]
