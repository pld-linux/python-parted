Summary:	Python module for parted
Summary(pl):	Modu³ Pythona dla Parteda
Name:		python-parted
Version:	1.6.9
Release:	2
License:	LGPL
Group:		Libraries
Source0:	pyparted-%{version}.tar.gz
# Source0-md5:	981718416c8f426d2472f51c859a126f
BuildRequires:	automake
BuildRequires:	parted-devel >= 1.6.22-3
BuildRequires:	python-devel >= 1:2.4
%pyrequires_eq	python-libs
Requires:	parted >= 1.6.22-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module for the parted library. It is used for manipulating
partition tables.

%description -l pl
Modu³ Pythona dla biblioteki parted. S³u¿y do modyfikowania tablic
partycji.

%prep
%setup -q -n pyparted-%{version}

%build
cp -f /usr/share/automake/config.* .
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
