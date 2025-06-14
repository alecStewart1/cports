pkgname = "rio"
pkgver = "0.2.18"
pkgrel = 0
build_type = "cargo"
make_build_args = [
    "-p rioterm",
    "--no-default-features", 
    "--features=wayland",
]
make_check_arags = ["cargo-auditable", "pkgconf"]
hostmakedepends = [
    "cargo-auditable", 
    "pkgconf", 
    "cmake", 
    "python3"
]
makedepends = [
    "rust-std",
    "freetype-devel",
    "expat-devel",
    "fontconfig-devel",
    "libxcb-devel"
]
pkgdesc = "A hardware-accelerated GPU terminal emulator focusing to run in desktops and browsers."
license = "MIT"
url = "https://rioterm.com/"
source = f"https://github.com/raphamorim/{pkgname}/archive/refs/tags/v{pkgver}.tar.gz"
sha265 = "ef0ce3a21210fbade1525e74d601f31439b2fb1d261e5456ca891ef80260ca57"

# TODO get man or docs from...somewhere?
def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/rio")
    self.install_license("LICENSE")
