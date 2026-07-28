Name:           qprompt
Version:        2.0.2
Release:        1%{?dist}
Summary:        Personal teleprompter software for video creators

License:        GPL-3.0-or-later AND CC-BY-4.0
URL:            https://qprompt.app/
Source0:        https://github.com/Cuperino/QPrompt-Teleprompter/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  extra-cmake-modules
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6ShaderTools)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6Core5Compat)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)

# Runtime QML modules that are not always detected automatically.
Requires:       qt6-qtdeclarative
Requires:       qt6-qtquickcontrols2
Requires:       kf6-kirigami

%description
QPrompt is a free and open-source teleprompter application for video creators.
It provides a convergent Qt and KDE Kirigami interface, rich-text editing,
mirroring, markers, timers, multi-screen support, and precise prompting
controls.

%prep
%autosetup -n QPrompt-Teleprompter-%{version} -p1

%build
%cmake \
    -DSOURCE_DEPENDENCIES_EXCLUSIVELY_FROM_SYSTEM=ON \
    -DBUILD_TESTING=OFF

%cmake_build

%install
%cmake_install

# Remove files that should not be packaged if upstream installs them.
find %{buildroot} -name '*.la' -delete

%check
# Validate installed desktop and AppStream metadata when present.
find %{buildroot}%{_datadir}/applications -name '*.desktop' -print0 2>/dev/null | \
    xargs -0 -r desktop-file-validate
find %{buildroot}%{_datadir}/metainfo %{buildroot}%{_datadir}/appdata \
    -name '*.xml' -print0 2>/dev/null | xargs -0 -r appstream-util validate-relax

%files
%{_bindir}/qprompt
%{_datadir}/applications/com.cuperino.qprompt.desktop
%{_datadir}/metainfo/com.cuperino.qprompt.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/doc/qprompt/
%{_mandir}/man1/qprompt.1*

%changelog
* Sat Jul 25 2026 COPR Builder <builder@example.invalid> - 2.0.2-1
- Initial COPR package for QPrompt 2.0.2
