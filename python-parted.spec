Summary:	Python module for parted library
Summary(pl.UTF-8):	Moduł Pythona do biblioteki parteda
Name:		python-parted
Version:	3.9
Release:	1
License:	GPL v2+
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
# Source0-md5:	f16c7ef7f5fa4a43fcb2a4654b487e39
URL:		https://fedorahosted.org/pyparted/
BuildRequires:	parted-devel >= 3.1
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-libs
Requires:	parted >= 3.1
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} -- setup.py install \
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
