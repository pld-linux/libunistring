Summary:	Unicode string library
Summary(pl.UTF-8):	Biblioteka do obsługi łańcuchów unikodowych
Name:		libunistring
Version:	1.0
Release:	1
License:	LGPL v3+ or GPL v2+
Group:		Libraries
Source0:	https://ftp.gnu.org/gnu/libunistring/%{name}-%{version}.tar.xz
# Source0-md5:	88752c7859212f9c7a0f6cbf7a273535
Patch0:		%{name}-info.patch
URL:		http://gnu.org/software/libunistring/
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo >= 4.12
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides functions for manipulating Unicode strings and
for manipulating C strings according to the Unicode standard.

%description -l pl.UTF-8
Ta biblioteka udostępnia funkcje do obsługi łańcuchów unikodowych oraz
do obsługi łańcuchów znaków C zgodnie ze standardem Unicode.

%package devel
Summary:	Header files for unistring library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki unistring
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for unistring library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki unistring.

%package static
Summary:	Static unistring library
Summary(pl.UTF-8):	Statyczna biblioteka unistring
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static unistring library.

%description static -l pl.UTF-8
Statyczna biblioteka unistring.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc in -devel
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libunistring

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	devel -p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libdir}/libunistring.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libunistring.so.2

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_libdir}/libunistring.so
%{_libdir}/libunistring.la
%{_includedir}/unistring
%{_includedir}/uni*.h
%{_infodir}/libunistring.info*

%files static
%defattr(644,root,root,755)
%{_libdir}/libunistring.a
