pkgname = "rio"
pkgver = "0.2.18"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features", 
    "--features=wayland",
]
make_check_args = ["cargo-auditable", "pkgconf"]
hostmakedepends = [
    "cargo-auditable", 
    "pkgconf", 
    "cmake", 
    "python"
]
makedepends = [
    "rust-std",
    "freetype-devel",
    "libexpat-devel",
    "fontconfig-devel",
    "libxcb-devel"
]
pkgdesc = "Hardware-accelerated GPU terminal emulator in Rust"
license = "MIT"
url = "https://rioterm.com"
source = f"https://github.com/raphamorim/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "ef0ce3a21210fbade1525e74d601f31439b2fb1d261e5456ca891ef80260ca57"


# TODO get man or docs from...somewhere?
def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rio")
    self.install_license("LICENSE")
