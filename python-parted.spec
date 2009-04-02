Summary:	Python module for parted
Summary(pl.UTF-8):	Moduł Pythona dla parteda
Name:		python-parted
Version:	2.0.9
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	https://fedorahosted.org/releases/p/y/pyparted/pyparted-%{version}.tar.gz
# Source0-md5:	74a0406e8e4b213507c4ad0e0912d969
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	parted-devel >= 1.6.22-3
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	parted >= 1.8.8
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
%{__libtoolize}
%{__autoheader}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/_pedmodule.so
%dir %{py_sitedir}/parted
%{py_sitedir}/parted/*.py[co]
