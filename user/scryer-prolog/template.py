pkgname = "scryer-prolog"
pkgver = "0.10.0"
pkgrel = 0
build_style = "cargo"
# link system libffi; the bundled libffi-sys build fails in the chroot
# (needs linux/limits.h, chokes on clang in its libtool probes)
make_build_args = ["--features", "libffi/system"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "openssl3-devel", "libffi8-devel"]
pkgdesc = "Modern Prolog implementation written mostly in Rust"
license = "BSD-3-Clause"
url = "https://codeberg.org/mthom/scryer-prolog"
source = f"{url}/archive/v{pkgver}.tar.gz"
sha256 = "a0b94a4a0c575bc085cc0f02b7a3dc14e928f08ce29b13d07684e7bb6445475b"
# too many of them need net
# completions with host bin
options = ["!check", "!cross"]

if self.profile.wordsize == 32:
    broken = "needs atomic64"


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "scryer-prolog"))
    self.install_license("LICENSE")
