Summary:	Python module for parted library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki parteda
Name:		python-parted
Version:	3.8
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
# Source0-md5:	e9cd0c94c71ac17755f71a8e1561eac2
URL:		https://fedorahosted.org/pyparted/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	parted-devel >= 2.2
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	parted >= 2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the parted library. It is used for manipulating
partition tables.

%description -l pl.UTF-8
Moduł Pythona dla biblioteki parted. Służy do modyfikowania tablic
partycji.

%prep
%setup -q -n pyparted-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python -- setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%attr(755,root,root) %{py_sitedir}/_pedmodule.so
%{py_sitedir}/pyparted-%{version}-py*.egg-info
%dir %{py_sitedir}/parted
%{py_sitedir}/parted/*.py[co]
