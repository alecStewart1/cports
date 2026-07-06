pkgname = "mise"
pkgver = "2026.7.0"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
    "--features=native-tls",
]
hostmakedepends = [
    "cargo-auditable",
    "cmake",
    "pkgconf",
]
makedepends = [
    "libgit2-devel",
    "lua5.1-devel",
    "openssl3-devel",
    "rust-std",
    "zstd-devel",
]
checkdepends = ["bash"]
pkgdesc = "Development environment setup tool"
license = "MIT"
url = "https://mise.jdx.dev"
source = f"https://github.com/jdx/mise/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "c2e581ac26551e324a2bdb726d6dd34356f865ebb4220d3998dc3f99de9ec42a"
# check: takes forever
options = ["!check"]

if self.profile().wordsize == 32:
    # lol
    broken = "memory allocation of 13107204 bytes failed"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/mise")
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
