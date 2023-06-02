# Maintainer: Whois Hoeless <whois@hoeless.com>

pkgname=dcsf
pkgver() {
  cd "$srcdir/Discord-Console-File-Upload"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}
pkgrel=1
pkgdesc="Send attachments / files to DMs with messages in Discord using the dcsf command in your command line. (dcsf = discord send file)"
arch=('any')
url="https://github.com/whois-hoeless/Discord-Console-File-Upload"
license=('MIT')
depends=('python>=3.9' 'git')

source=("git+https://github.com/whois-hoeless/Discord-Console-File-Upload")

package() {
    cd "$srcdir"
    install -Dm755 dcsf "$pkgdir/usr/bin/dcsf"
    install -Dm644 .env "/home/$USER/.config/dcsf/.env"
    cd "$srcdir/Discord-Console-File-Upload"
    pip install -r requirements.txt
}