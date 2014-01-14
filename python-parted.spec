#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	parted
Summary:	Python module for parted library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki parteda
Name:		python-%{module}
Version:	3.10
Release:	3
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
# Source0-md5:	d494440b34bc9ea0afea45c4a4ac3274
URL:		https://fedorahosted.org/pyparted/
BuildRequires:	parted-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	parted >= 3.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the parted library. It is used for manipulating
partition tables.

%description -l pl.UTF-8
Moduł Pythona dla biblioteki parted. Służy do modyfikowania tablic
partycji.

%package -n python3-%{module}
Summary:	Python module for parted library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki parteda
Group:		Libraries/Python

%description -n python3-%{module}
Python module for the parted library. It is used for manipulating
partition tables.

%description -n python3-%{module} -l pl.UTF-8
Moduł Pythona dla biblioteki parted. Służy do modyfikowania tablic
partycji.

%prep
%setup -q -n pyparted-%{version}

%build
%if %{with python2}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python} setup.py build --build-base build-2
%endif

%if %{with python3}
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py build --build-base build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%{__python} setup.py \
	build --build-base build-2 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean
%endif

%if %{with python3}
%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/_ped.so
%dir %{py_sitedir}/parted
%{py_sitedir}/parted/*.py[co]
%{py_sitedir}/pyparted-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{py3_sitedir}/_ped.*.so
%dir %{py3_sitedir}/parted
%{py3_sitedir}/parted/*.py
%{py3_sitedir}/parted/__pycache__
%{py3_sitedir}/pyparted-%{version}-py*.egg-info
%endif
