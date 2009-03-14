Summary:	Python module for parted
Summary(pl.UTF-8):	Moduł Pythona dla parteda
Name:		python-parted
Version:	1.8.9
Release:	3
License:	LGPL
Group:		Libraries/Python
Source0:	http://dcantrel.fedorapeople.org/pyparted/pyparted-%{version}.tar.bz2
# Source0-md5:	24d60b03142abd7cf1ba4d069bc9db3e
Patch0:		%{name}-constraint.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	parted-devel >= 1.6.22-3
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	parted >= 1.8.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the parted library. It is used for manipulating
partition tables.

%description -l pl.UTF-8
Moduł Pythona dla biblioteki parted. Służy do modyfikowania tablic
partycji.

%prep
%setup -q -n pyparted-%{version}
%patch0 -p1

%build
%{__make} \
	AM_CFLAGS="-fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{py_sitedir}/partedmodule.so
