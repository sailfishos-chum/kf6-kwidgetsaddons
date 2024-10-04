%global  kf_version 6.6.0

Name:		kf6-kwidgetsaddons
Version:	6.6.0
Release:	0%{?dist}
Summary:	KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets
License:	BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later
URL:		https://invent.kde.org/frameworks/%{framework}
Source0:    %{name}-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	clang
BuildRequires:	kf6-extra-cmake-modules >= %{kf_version}
BuildRequires:	kf6-rpm-macros
BuildRequires:	qt6-qtbase-devel
BuildRequires:	qt6-qttools-devel
BuildRequires:	qt6-qttools-static
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	fdupes


%description
KDE Frameworks 6 Tier 1 addon with various classes on top of QtWidgets.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	qt6-qtbase-devel
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version}/upstream -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang_kf6 kwidgetsaddons6_qt
%fdupes %{buildroot}/%{_kf6_includedir}/KWidgetsAddons/
%fdupes LICENSES

%files -f kwidgetsaddons6_qt.lang
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/libKF6WidgetsAddons.so.*
%{_kf6_datadir}/qlogging-categories6/*categories

%files devel
%{_kf6_includedir}/KWidgetsAddons/
%{_kf6_libdir}/libKF6WidgetsAddons.so
%{_kf6_libdir}/cmake/KF6WidgetsAddons/
%{_kf6_qtplugindir}/designer/kwidgetsaddons6widgets.so
%{_qt6_docdir}/*.tags

%files doc
%{_qt6_docdir}/*.qch
