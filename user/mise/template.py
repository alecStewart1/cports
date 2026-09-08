pkgname = "mise"
pkgver = "2026.9.9"
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
sha256 = "96b461a471c9f35985611352b9d2c40cd7e66cc52496b1ad9bb64712fec677b2"
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
