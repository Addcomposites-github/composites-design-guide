{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.nodejs_20
    pkgs.nodePackages.npm
    # System libraries needed by weasyprint
    pkgs.cairo
    pkgs.pango
    pkgs.gdk-pixbuf
    pkgs.gobject-introspection
    pkgs.pkg-config
  ];
}
