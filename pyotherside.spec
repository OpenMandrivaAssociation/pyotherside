%global debug_package %{nil}

Name:    pyotherside
Version: 1.5.9
Release: 3
Summary: Asynchronous Python 3 Bindings for Qt 5
Group:   Development/KDE and Qt
License: ISC
URL:     https://github.com/thp/pyotherside/
Source0: https://github.com/thp/pyotherside/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: pkgconfig(Qt5Svg)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: python3dist(sphinx)
BuildRequires: qt5-qtbase-devel
BuildRequires: x11-server-xvfb

%description
A Qt 5 QML Plugin that provides access to a Python 3 interpreter from QML.

%prep
%autosetup -p1

%build
%qmake_qt5
%make_build
%make_build -C docs SPHINXBUILD=sphinx-build html

%check
# Tests require an X server, although it doesn't seem to be used for much
xvfb-run tests/tests

%install
%make_install INSTALL_ROOT="$RPM_BUILD_ROOT"
rm -rf %{buildroot}%{_qt5_testsdir}

%files
%{_libdir}/qt5/qml/io/thp/pyotherside/libpyothersideplugin.so
%{_libdir}/qt5/qml/io/thp/pyotherside/pyotherside.qmltypes
%{_libdir}/qt5/qml/io/thp/pyotherside/qmldir
%{_libdir}/qt5/tests/qtquicktests/qtquicktests
%doc docs/_build/html
%license LICENSE
%doc README
