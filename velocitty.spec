Name:		velocitty
Version:	1.0.4
Release:	2
Summary:	Terminal emulator for Linux desktops.  An easy-to-use terminal emulator.
License:        GPL-3+,MIT
URL:            https://github.com/xapp-project/velocitty
Source0:	https://github.com/xapp-project/velocitty/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  lib64glib2.0-devel
BuildRequires:  lib64gio-gir2.0
BuildRequires:  lib64gtk4_1
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:	lib64adwaita-gir
Requires:       xapp-symbolic-icons
Requires:	lib64gtk-gir4.0
Requires:	lib64vte-gir3.91
Requires:       python
Requires:       python-gi
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       fcitx5-gtk4

%description
Terminal emulator for Linux desktops.  An easy-to-use terminal emulator.

%prep
%autosetup -p1

%files
%license LICENSES/*
%doc README.md
%{_bindir}/velocitty
%{python_sitelib}/velocitty/
%{_datadir}/velocitty/
%{_datadir}/applications/org.x.velocitty.desktop
%{_datadir}/icons/hicolor/scalable/apps/velocitty.svg
%{_datadir}/glib-2.0/schemas/org.x.velocitty.gschema.xml
