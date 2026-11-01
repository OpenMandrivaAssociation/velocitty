Name:		velocitty
Version:	1.0.4
Release:	1
Summary:	Terminal emulator for Linux desktops.  An easy-to-use terminal emulator.
License:        GPL-3+,MIT
URL:            https://github.com/xapp-project/velocitty
Source0:	https://github.com/xapp-project/velocitty/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Group:		Graphical desktop/Other

BuildSystem:    meson

BuildRequires:  gettext
BuildRequires:  gtk4.0
BuildRequires:  python-rpm
BuildRequires:  desktop-file-utils

Requires:       gtk4.0
Requires:       hicolor-icon-theme
Requires:       lib64adwaita-gir
Requires:       python-gobject3
Requires:       python-setproctitle
Requires:       python-xapp
Requires:       lib64vte-gtk4_2.91_0
Requires:       xapp-symbolic-icons
Requires:	fcitx5-gtk4
%description
Terminal emulator for Linux desktops.  An easy-to-use terminal emulator.

%prep
%autosetup -p1

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.x.velocitty.desktop

%files
%license LICENSES/*
%doc README.md
%{_bindir}/velocitty
%{python_sitelib}/velocitty/
%{_datadir}/velocitty/
%{_datadir}/applications/org.x.velocitty.desktop
%{_datadir}/icons/hicolor/scalable/apps/velocitty.svg
%{_datadir}/glib-2.0/schemas/org.x.velocitty.gschema.xml
