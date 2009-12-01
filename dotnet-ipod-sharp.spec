%include	/usr/lib/rpm/macros.mono
Summary:	.NET support for iPods
Summary(pl.UTF-8):	Obsługa iPodów z poziomu .NET
Name:		dotnet-ipod-sharp
Version:	0.8.5
Release:	1
# no real license information, just included COPYING
License:	LGPL v2
Group:		Libraries
Source0:	http://banshee-project.org/files/ipod-sharp/0.8.5/ipod-sharp-%{version}.tar.bz2
# Source0-md5:	fb7f53f64d825847d578a637cd48dd41
Patch0:		%{name}-dep.patch
Patch1:		%{name}-gac.patch
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
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ia64 mips ppc s390 s390x sparc sparcv9
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

%package devel
Summary:	Development files for ipod-sharp library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki ipod-sharp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for ipod-sharp library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki ipod-sharp.

%prep
%setup -q -n ipod-sharp-%{version}
%patch0 -p1
%patch1 -p1

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

# replace duplicates by symlinks
cd $RPM_BUILD_ROOT%{_prefix}/lib/ipod-sharp
for f in ipod-sharp.dll* ipod-sharp-ui.dll* ; do
	%{__rm} $f
	ln -sf ../mono/gac/ipod-sharp*/*/$f $f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%dir %{_prefix}/lib/ipod-sharp
%{_prefix}/lib/ipod-sharp/ipod-sharp-firmware.dll*
%{_prefix}/lib/mono/gac/ipod-sharp
%{_prefix}/lib/mono/gac/ipod-sharp-ui

%files devel
%defattr(644,root,root,755)
%{_prefix}/lib/ipod-sharp/ipod-sharp.dll*
%{_prefix}/lib/ipod-sharp/ipod-sharp-ui.dll*
%{_pkgconfigdir}/ipod-sharp.pc
%{_pkgconfigdir}/ipod-sharp-ui.pc
%{_libdir}/monodoc/sources/ipod-sharp-docs.*
