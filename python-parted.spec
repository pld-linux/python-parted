Summary:	python module for parted
Name:		python-parted
Version:	1.6.9
Release:	1
License:	GPL
Group:		System Environment/Libraries
Source0:	pyparted-%{version}.tar.gz
# Source0-md5:	981718416c8f426d2472f51c859a126f
BuildRequires:	parted-devel >= 1.6.12
BuildRequires:	python-devel
Requires:	parted >= 1.6.12
Requires:	python >= %(%{__python} -c "import sys; print sys.version[:3]")
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python modules for the parted library.  It is used for manipulation
partition tables.

%prep
%setup -q -n pyparted-%{version}

%build
mv configure.in configure.old
# test code is shitworth and it fails to link
grep -v 'AC_CHECK_LIB' configure.old > configure.in
rm configure.old

%{__autoconf}
%configure --with-python-version=2.4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/python?.?/site-packages/
%{_libdir}/python?.?/site-packages/*.so
