Summary:	An open and free bittorrent tracker
Name:		opentracker
Version:	0.cvs20090825
Release:	%mkrel 1
License:	Copyright only
Group:		Networking/File transfer
URL:		http://erdgeist.org/arts/software/opentracker/
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
opentracker is a open and free bittorrent tracker project. It aims for minimal 
resource usage and is intended to run at your wlan router. Currently it is 
deployed as an open and free tracker instance. Read our free and open tracker 
blog (http://opentracker.blog.h3q.com/) and do not hesitate to setup your own 
free trackers!.

%prep
%setup -q

%build
%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sysconfdir}
install -m 644 %{name}.conf.sample %{buildroot}%{_sysconfdir}/%{name}.conf
%make PREFIX=%{buildroot}%{_prefix} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README_v6 README
%{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
