%if 0%{?with_debug}
%global debug_package   %{nil}
%endif

Name:           dde-session-shell
Version:        5.0.0.8
Release:        3
Summary:        deepin-session-shell - Deepin desktop-environment - session-shell module
License:        GPLv3+
URL:            http://shuttle.corp.deepin.com/cache/repos/eagle/release-candidate/RERFNS4wLjAuNzYxMA/pool/main/d/dde-session-shell/
Source0:        %{name}_%{version}.orig.tar.xz
Patch0:		0001-fix-compile-error-for-openeuler.patch		

BuildRequires:  cmake
BuildRequires:  dde-daemon
BuildRequires:  dtkcore-devel
BuildRequires:  gsettings-qt
BuildRequires:  startdde
BuildRequires:  qt5-linguist
BuildRequires:  dtkwidget-devel
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
BuildRequires:  lightdm-qt5-devel lightdm-gtk-greeter

%description
deepin-session-shell - Deepin desktop-environment - session-shell module.

%prep
%autosetup -n %{name}-%{version} -p1

%build
export PATH=$PATH:%{_qt5_bindir}
cmake_version=$(cmake --version | head -1 | awk '{print $3}')
sed -i "s|VERSION 3.13.4|VERSION $cmake_version|g" CMakeLists.txt
%{__cmake} .
make

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
* Wed Sep 09 2020 chenbo.pan <panchenbo@uniontech.com> - 5.0.0.8-3
- fix compile error 

* Fri Sep 04 2020 chenbo.pan <panchenbo@uniontech.com> - 5.0.0.8-2
- fix compile error

* Thu Jul 30 2020 openEuler Buildteam <buildteam@openeuler.org> - 5.0.0.8-1
- Package init
