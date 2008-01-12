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
Patch0:		%{name}-dep.patch
URL:		http://banshee-project.org/Subprojects/Ipod-sharp
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.9
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.0
BuildRequires:	dotnet-ndesk-dbus-sharp-devel
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Suggests:	podsleuth >= 0.6.1
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
%setup -q -n ipod-sharp-%{version}
%patch0 -p1

%build
%{__aclocal} -I .
%{__autoconf}
%{__automake}
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
#%files devel
%{_pkgconfigdir}/ipod-sharp.pc
%{_pkgconfigdir}/ipod-sharp-ui.pc
#%{_libdir}/monodoc/sources/ipod-sharp-docs.*
