Name:		velocitty
Version:	1.0.7
Release:	1
Summary:	Terminal emulator for Linux desktops.  An easy-to-use terminal emulator.
License:        GPL-3+,MIT
URL:            https://github.com/xapp-project/velocitty
Source0:	https://github.com/xapp-project/velocitty/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  typelib(Gio)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python

Requires:	typelib(Adw)
Requires:       xapp-symbolic-icons
Requires:	typelib(Gtk)
Requires:	typelib(Vte)
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
