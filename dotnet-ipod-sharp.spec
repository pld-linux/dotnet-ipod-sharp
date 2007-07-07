#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET support for iPods
Name:		dotnet-ipod-sharp
Version:	0.6.3
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://banshee-project.org/files/ipod-sharp/ipod-sharp-%{version}.tar.gz
# Source0-md5:	c35131c3350e686d4a006377c1711834
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libipoddevice-devel >= 0.5.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipod-sharp provies support for high level features of Apple's iPod,
like support for audio content, including reading and writing of
the iTunes/iPod database, and syncing music. ipod-sharp also provides
a CIL wrapper for libipoddevice.

%prep
%setup -qn ipod-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/ipod-sharp
%{_pkgconfigdir}/ipod-sharp*.pc
