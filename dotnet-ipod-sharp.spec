%include	/usr/lib/rpm/macros.mono
Summary:	.NET support for iPods
Summary(pl.UTF-8):	Obsługa iPodów z poziomu .NET
Name:		dotnet-ipod-sharp
Version:	0.8.0
Release:	1
# no real license information, just included COPYING
License:	LGPL v2
Group:		Libraries
Source0:	http://banshee-project.org/files/ipod-sharp/ipod-sharp-%{version}.tar.gz
# Source0-md5:	ecb58c18599035fca34935a1287584f3
URL:		http://banshee-project.org/Subprojects/Ipod-sharp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	podsleuth
BuildRequires:	rpmbuild(monoautodeps)
ExcludeArch:	i386
# can't be noarch because of pkgconfigdir (use /usr/share/pkgconfig?)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ipod-sharp provides support for high level features of Apple's iPod,
like support for audio content, including reading and writing of
the iTunes/iPod database, and syncing music. ipod-sharp also provides
a CIL wrapper for libipoddevice.

%description -l pl.UTF-8
ipod-sharp zapewnia obsługę wysokopoziomowych możliwości urządzeń
Apple iPod, takich jak obsługa danych dźwiękowych wraz z odczytem i
zapisem baz danych iTunes/iPod oraz synchronizacja muzyki. ipod-sharp
udostępnia także wrapper CIL dla libipoddevice.

%prep
%setup -qn ipod-sharp-%{version}

%build
%{__libtoolize}
%{__aclocal} -I .
%{__autoconf}
%{__automake}
echo foo
%configure

%{__make} -j1

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
%{_pkgconfigdir}/ipod-sharp.pc
%{_pkgconfigdir}/ipod-sharp-ui.pc
