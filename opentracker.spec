Summary:		An open and free bittorrent tracker
Name:			opentracker
Version:		0.cvs20090825
Release:		%mkrel 4
License:		Copyright only
Group:			Networking/File transfer
URL:			http://erdgeist.org/arts/software/opentracker/
Source0:		%{name}-%{version}.tar.bz2
Source1:		%{name}.init
Patch0:			opentracker-0.cvs20090825-conf-fix.patch
Patch1:			opentracker-0.cvs20090825-daemon-fix.patch
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	zlib-devel
BuildRequires:	libowfat-devel

%description
opentracker is a open and free bittorrent tracker project. It aims for minimal 
resource usage and is intended to run at your wlan router. Currently it is 
deployed as an open and free tracker instance. Read our free and open tracker 
blog (http://opentracker.blog.h3q.com/) and do not hesitate to setup your own 
free trackers!.

%prep
%setup -q
%patch0 -p1 -b .conf-fix
%patch1 -p1 -b .daemon-fix

%build
#-DWANT_V6
export FEATURES="-DWANT_SYNC_LIVE -DWANT_ACCESSLIST_WHITE -DWANT_SYNC_SCRAPE -DWANT_COMPRESSION_GZIP -DWANT_RESTRICT_STATS -DWANT_IP_FROM_PROXY"
%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/%{name} %buildroot%{_initrddir}

%make PREFIX=%{buildroot}%{_prefix} install

install -D -m 644 %{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -D -m 755 %{SOURCE1} %buildroot%{_initrddir}/%{name}

touch %{buildroot}%{_sysconfdir}/%{name}/whitelist.conf

%clean
rm -rf %{buildroot}

%post
%_post_service opentracker

%preun
%_preun_service opentracker

%files
%defattr(-,root,root)
%doc README_v6 README
%dir %{_sysconfdir}/%{name}
%{_sysconfdir}/%{name}/%{name}.conf
%{_sysconfdir}/%{name}/whitelist.conf
%{_initrddir}/%{name}
%{_bindir}/%{name}
