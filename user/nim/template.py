pkgname = "nim"
pkgver = "2.2.10"
pkgrel = 0
build_style = "makefile"
pkgdesc = "Statically typed, compiled systems programming language"
license = "MIT"
url = "https://nim-lang.org"

# pinned to whatever the upstream tarball's koch.nim says; bump on version update
_atlas_commit = "ff1f4289482dce94ba9f95b3b0ae16d16e21eb3d"  # atlas 0.10.1
_sat_commit = "e63eaea8baf00bed8bcd5a29ffd8823abb265b39"

source = [
    f"{url}/download/nim-{pkgver}.tar.xz",
    f"https://github.com/nim-lang/atlas/archive/{_atlas_commit}.tar.gz",
    f"https://github.com/nim-lang/sat/archive/{_sat_commit}.tar.gz",
]
source_paths = [
    "",
    "dist/atlas",
    "dist/atlas/dist/sat",
]
sha256 = [
    "7957b7ed004206bcf10bcc4f3b4744153878e62f2431552a9a8e9d3f40e8d5d5",
    "2ddd9a6fc549c7c59dbae8b02882fd77e4bd7858a2edd97d6e3450debfb11535",
    "0846607e21cc2980ce68325fc3b4acbf2ebe4c74cbc5ee1c459fbc2abaf72856",
]
options = ["!check", "etcfiles"]


def build(self):
    # tarball ships pre-transpiled c_code/, so plain make gives us a
    # C-compiled bootstrap. koch boot then rebuilds bin/nim in itself.
    # atlas+sat are vendored above so koch tools' cloneDependency sees
    # dist/atlas/ and skips the network clone.
    self.make.build([])

    self.do(
        "bin/nim", "c", "-d:release",
        "--skipUserCfg", "--skipParentCfg", "--hints:off",
        "koch",
    )
    self.do(
        "./koch", "boot", "-d:release",
        "--skipUserCfg", "--skipParentCfg", "--hints:off",
    )
    self.do(
        "./koch", "tools",
        "--skipUserCfg", "--skipParentCfg", "--hints:off",
    )


def install(self):
    self.install_bin("bin/nim")
    for tool in ("nimble", "nimsuggest", "nimpretty", "atlas", "testament"):
        self.install_bin(f"bin/{tool}")

    # stdlib path is hardcoded: /usr/bin/nim -> prefix=/usr/lib/nim,
    # libpath=prefix/"lib" (compiler/options.nim getPrefixDir)
    self.install_files("lib", "usr/lib/nim/lib")
    self.install_files("config", "etc/nim")
    self.install_files("doc", "usr/share/doc/nim")

    self.install_license("copying.txt")


@subpackage("nim-tools")
def _(self):
    self.depends = [self.parent]
    self.subdesc = "Companion tools for the Nim compiler"
    # nimgrep needs pcre v1; chimera only has pcre2
    return [
        "cmd:nimble",
        "cmd:nimsuggest",
        "cmd:nimpretty",
        "cmd:atlas",
        "cmd:testament",
    ]