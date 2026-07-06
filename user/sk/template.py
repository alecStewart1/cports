pkgname = "sk"
pkgver = "5.1.0"
pkgrel = 0
build_style = "cargo"
hostmakedepends = ["cargo-auditable"]
makedepends = ["rust-std"]
pkgdesc = "Fuzzy Finder in rust!"
license = "MIT"
url = "https://github.com/skim-rs/skim"
source = f"{url}/archive/refs/tags/v{pkgver}.tar.gz"
source_paths = ["."]
sha256 = "9f3d8226114b7f76e78b2a4b2819c7a23694528bd06a3f05e02e6c9667143d33"


def post_install(self):
    self.install_license("LICENSE")
    self.install_man("man/man1/sk.1")
    self.install_file("plugin/skim.vim", "usr/share/vim/vimfiles/plugin")
    self.install_file("plugin/skim.vim", "usr/share/nvim/runtime/plugin")
    self.install_bin("bin/sk-tmux")
    self.install_man("man/man1/sk-tmux.1")

    with self.pushd("shell"):
        self.install_completion("completion.bash", "bash")
        self.install_completion("completion.fish", "fish")
        self.install_completion("completion.zsh", "zsh")
        self.install_completion("completion.nu", "nushell")

        for ext in ["bash", "fish", "zsh"]:
            self.install_file(f"key-bindings.{ext}", "usr/share/sk")


@subpackage("sk-tmux")
def _(self):
    self.subdesc = "tmux integration script"
    self.depends = [self.parent, "bash", "tmux"]
    self.install_if = [self.parent, "bash", "tmux"]

    return ["cmd:sk-tmux"]
