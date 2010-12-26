Summary: An open and free bittorrent tracker
Name: opentracker
Version: 0.cvs20100808
Release: %mkrel 1
License: Copyright only
Group: Networking/File transfer
URL: http://erdgeist.org/arts/software/opentracker/
Source0: %{name}-%{version}.tar.bz2
Source1: %{name}.init
Source2: %{name}.conf.http
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: zlib-devel
BuildRequires: libowfat-devel

%description
opentracker is a open and free bittorrent tracker project. It aims for minimal 
resource usage and is intended to run at your wlan router. Currently it is 
deployed as an open and free tracker instance. Read our free and open tracker 
blog (http://opentracker.blog.h3q.com/) and do not hesitate to setup your own 
free trackers!

%prep
%setup -q

%build
# Some experimental or older, deprecated features can be enabled by the -DWANT_LOG_NETWORKS, -DWANT_SYNC_SCRAPE or -DWANT_IP_FROM_PROXY switch.
# -DWANT_V6 makes opentracker an IPv6-only tracker.
# Normally opentracker tracks any torrent announced to it.
# You can change that behaviour by enabling ONE of -DWANT_ACCESSLIST_BLACK or -DWANT_ACCESSLIST_WHITE.
# Some statistics opentracker can provide are sensitive. You can restrict access to these statistics by enabling -DWANT_RESTRICT_STATS.
# opentracker can run in a cluster. Enable this behaviour by enabling -DWANT_SYNC_LIVE.
export FEATURES=" -DWANT_COMPRESSION_GZIP -DWANT_IP_FROM_QUERY_STRING"
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}/%{name} %{buildroot}%{_initrddir}
%make PREFIX=%{buildroot}%{_prefix} install
install -D -m 644 %{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -D -m 755 %{SOURCE1} %{buildroot}%{_initrddir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d
install -D -m 755 %{SOURCE2} %{buildroot}%{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
#touch %{buildroot}%{_sysconfdir}/%{name}/whitelist.conf

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
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf/webapps.d/%{name}.conf
#{_sysconfdir}/%{name}/whitelist.conf
%{_initrddir}/%{name}
%{_bindir}/%{name}


%changelog
* Sat Aug 29 2009 Raphaël Gertz <rapsys@mandriva.org> 0.cvs20090825-3mdv2010.0
+ Revision: 422324
- Fix condrestart
- Fix again initscript for translation
- Fix init script
- Update init script
- Rebuild

* Sat Aug 29 2009 Raphaël Gertz <rapsys@mandriva.org> 0.cvs20090825-1mdv2010.0
+ Revision: 422211
- Add zlib buildrequires
- Add libowfat-devel build requires
- Add fork feature
  Fix init script
  Fix conf
- First release
- First partial version (miss initscript)
- Change package name
- Created package structure for xbtt.
