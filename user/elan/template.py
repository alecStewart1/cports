pkgname = "elan"
pkgver = "4.2.4"
pkgrel = 1
build_style = "cargo"
# no-self-update: elan's built-in self-updater must not fight apk
make_build_args = ["--features", "no-self-update"]
hostmakedepends = ["cargo-auditable", "pkgconf"]
makedepends = ["rust-std", "curl-devel"]
pkgdesc = "Toolchain manager for the Lean theorem prover"
license = "MIT OR Apache-2.0"
url = "https://github.com/leanprover/elan"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "aae972bd10907763d53d0ea9593c02a340359505ce667b99e5289372f6801eec"
# no test suite that runs outside of upstream CI; also proxies need
# toolchains to exercise, which is a network operation
options = ["!check"]

# the built binary is elan-init; elan and the tool proxies are the same
# binary dispatching on argv[0] (see src/elan-cli/main.rs)
_tools = ["lean", "leanpkg", "leanchecker", "leanc", "leanmake", "lake"]


def install(self):
    from cbuild.util import cargo

    self.install_bin(cargo.target_path(self, "elan-init"), name="elan")
    for tool in _tools:
        self.install_link(f"usr/bin/{tool}", "elan")
    self.install_license("LICENSE-MIT")
    self.install_license("LICENSE-APACHE")
