Name:           dde-session-shell
Version:        5.3.0.40.2
Release:        1
Summary:        deepin-session-shell - Deepin desktop-environment - session-shell module
License:        GPLv3+
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/RERFNS4wLjAuNzYxMA/pool/main/d/dde-session-shell/
Source0:        %{name}_%{version}.orig.tar.xz

BuildRequires:  cmake
BuildRequires:  dde-daemon
BuildRequires:  dtkcore-devel
BuildRequires:  gsettings-qt
BuildRequires:  startdde
BuildRequires:  qt5-linguist
BuildRequires:  dtkwidget-devel >= 5.1
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXi-devel
BuildRequires:  xcb-util-wm xcb-util-wm-devel
BuildRequires:  dde-qt-dbus-factory-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  lightdm-qt5-devel
BuildRequires:  pam-devel
Requires:       lightdm
Requires(post): sed
Provides:       lightdm-deepin-greeter = %{version}-%{release}
Provides:       lightdm-greeter = 1.2

%description
deepin-session-shell - Deepin desktop-environment - session-shell module.

%prep
%setup -q -n %{name}-%{version}

%build
export PATH=$PATH:%{_qt5_bindir}
cmake_version=$(cmake --version | head -1 | awk '{print $3}')
sed -i "s|VERSION 3.13.4|VERSION $cmake_version|g" CMakeLists.txt
%cmake
%make_build

%install
%make_install

%files
%{_bindir}/dde-lock
%{_bindir}/dde-shutdown
%{_bindir}/lightdm-deepin-greeter
%attr(755,root,root) %{_bindir}/deepin-greeter
%{_sysconfdir}/deepin/greeters.d/00-xrandr
%{_sysconfdir}/deepin/greeters.d/lightdm-deepin-greeter
%{_datadir}/dde-session-shell/

%{_datadir}/xgreeters/lightdm-deepin-greeter.desktop
%{_datadir}/dbus-1/services/com.deepin.dde.lockFront.service
%{_datadir}/dbus-1/services/com.deepin.dde.shutdownFront.service

%changelog
* Thu Jul 08 2021 weidong <weidong@uniontech.com> - 5.3.0.40.2-1
- Update 5.3.0.40.2

* Wed Sep 09 2020 chenbo.pan <panchenbo@uniontech.com> - 5.0.0.8-4
- fix compile error for openeuler 

* Fri Sep 04 2020 weidong <weidong@uniontech.com> - 5.0.0.8-3
- fix source url in spec

* Fri Sep 04 2020 chenbo.pan <panchenbo@uniontech.com> - 5.0.0.8-2
- fix compile error

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.0.8-1
- Package init
