pkgname = "mise"
pkgver = "2026.9.13"
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
sha256 = "5e3cfaeb4cfaba656fb7532759e8a268da965a76646869ca2215465a4e99aa22"
# check: takes forever
options = ["!check"]

if self.profile.wordsize == 32:
    # lol
    broken = "memory allocation of 13107204 bytes failed"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "mise"))
    self.install_license("LICENSE")
    self.install_man("man/man1/mise.1")
