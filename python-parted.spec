Summary:	Python module for parted
Summary(pl.UTF-8):	Moduł Pythona dla parteda
Name:		python-parted
Version:	1.6.10
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	pyparted-%{version}.tar.gz
# Source0-md5:	977f05d390a9198a1170f860977ebcc6
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	parted-devel >= 1.6.22-3
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python-libs
Requires:	parted >= 1.6.22-3
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
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-python-version=2.4
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
