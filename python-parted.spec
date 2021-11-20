#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	parted
Summary:	Python 2.x bindings for libparted library
Summary(pl.UTF-8):	Wiązania Pythona 2.x do biblioteki libparted
Name:		python-%{module}
Version:	3.11.2
Release:	4
License:	GPL v2+
Group:		Libraries/Python
#Source0Download: https://github.com/dcantrell/pyparted/releases
Source0:	https://github.com/dcantrell/pyparted/releases/download/v%{version}/pyparted-%{version}.tar.gz
# Source0-md5:	9477016f5a00bd2d7a280879cdeec3a4
Patch0:		gcc10.patch
URL:		https://github.com/dcantrell/pyparted
BuildRequires:	parted-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-modules >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	parted >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2.x bindings for the libparted library. It is used for
manipulating partition tables.

%description -l pl.UTF-8
Wiązania Pythona 2.x do biblioteki libparted. Służy do modyfikowania
tablic partycji.

%package -n python3-%{module}
Summary:	Python 3.x bindings for libparted library
Summary(pl.UTF-8):	Wiązania Pythona 3.x do biblioteki libparted
Group:		Libraries/Python
Requires:	parted >= 3.1

%description -n python3-%{module}
Python 3.x bindings for the libparted library. It is used for
manipulating partition tables.

%description -n python3-%{module} -l pl.UTF-8
Wiązania Pythona 3.x do biblioteki libparted. Służy do modyfikowania
tablic partycji.

%prep
%setup -q -n pyparted-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{py_sitedir}/_ped.so
%dir %{py_sitedir}/parted
%{py_sitedir}/parted/*.py[co]
%{py_sitedir}/pyparted-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{py3_sitedir}/_ped.*.so
%dir %{py3_sitedir}/parted
%{py3_sitedir}/parted/*.py
%{py3_sitedir}/parted/__pycache__
%{py3_sitedir}/pyparted-%{version}-py*.egg-info
%endif
