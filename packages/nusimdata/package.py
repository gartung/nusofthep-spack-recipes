# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
from spack.pkg.fnal_art.fnal_github_package import *


class Nusimdata(CMakePackage, FnalGithubPackage):
    """Nusimdata"""

    repo = "NuSoftHEP/nusimdata"
    license("Apache-2.0")
    version_patterns = ["v1_24_05", "1.27.02"]

    version("develop", branch="develop", get_full_repo=True)
    version("1.28.06", sha256="665414d78ca06b13a48369262ceac3db0f9d46a9df4f2310d81c5de1bf6668b0")
    version("1.27.02", sha256="ed61e94ef931ed6383299db281c54df82136dfe5331492072ac1a3f08770b6a8")

    cxxstd_variant("17", "20", default="17")

    # Build and link dependencies.
    depends_on("cetmodules", type="build")

    depends_on("canvas")
    depends_on("canvas-root-io")
    depends_on("cetlib-except")
    depends_on("dk2nudata")
    depends_on("nufinder", when="@1.27.02:")
    depends_on("root")

    @cmake_preset
    def cmake_args(self):
        return [self.define_from_variant("CMAKE_CXX_STANDARD", "cxxstd")]
