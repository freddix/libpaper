Summary:	Library for handling paper characteristics
Name:		libpaper
Version:	1.1.24
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://ftp.debian.org/debian/pool/main/libp/libpaper/%{name}_%{version}.tar.gz
# Source0-md5:	5bc87d494ba470aba54f6d2d51471834
URL:		http://packages.debian.org/unstable/source/libpaper
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libpaper paper-handling library automates recognition of many
different paper types and sizes for programs that need to deal with
printed output.

%package devel
Summary:	Header files for libpaper library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libpaper library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
echo '# See papersize(5) for possible values\na4' > $RPM_BUILD_ROOT%{_sysconfdir}/papersize

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%config(noreplace,missingok) %verify(not md5 mtime size) %{_sysconfdir}/papersize
%attr(755,root,root) %{_bindir}/paperconf
%attr(755,root,root) %{_sbindir}/paperconfig
%attr(755,root,root) %ghost %{_libdir}/libpaper.so.1
%attr(755,root,root) %{_libdir}/libpaper.so.*.*.*
%{_mandir}/man1/paperconf.1*
%{_mandir}/man5/papersize.5*
%{_mandir}/man8/paperconfig.8*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libpaper.so
%{_includedir}/paper.h
%{_mandir}/man3/*.3*

