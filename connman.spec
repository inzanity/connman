# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.23
# 
# >> macros
# << macros

Name:       connman
Summary:    Connection Manager
Version:    0.77.3
Release:    1
Group:      Communications/ConnMan
License:    GPLv2
URL:        http://connman.net/
Source0:    http://www.kernel.org/pub/linux/network/connman/connman-%{version}.tar.bz2
Source100:  connman.yaml
Requires:   dbus
Requires:   wpa_supplicant >= 0.7.1
Requires:   bluez
Requires:   ofono
Requires:   pacrunner
Requires:   ntp
Requires:   systemd
Requires(preun): systemd
Requires(post): systemd
Requires(postun): systemd
BuildRequires:  pkgconfig(libiptc)
BuildRequires:  pkgconfig(xtables)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libudev) >= 145
BuildRequires:  openconnect
BuildRequires:  openvpn


%description
Connection Manager provides a daemon for managing Internet connections
within embedded devices running the Linux operating system.



%package devel
Summary:    Development files for Connection Manager
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
connman-devel contains development files for use with connman.

%package test
Summary:    Test Scripts for Connection Manager
Group:      Development/Tools
Requires:   %{name} = %{version}-%{release}
Requires:   dbus-python
Requires:   pygobject2

%description test
Scripts for testing Connman and its functionality


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static \
    --enable-ethernet=builtin \
    --enable-wifi=builtin \
    --enable-ofono=builtin \
    --enable-bluetooth=builtin \
    --enable-loopback=builtin \
    --enable-dnsproxy=builtin \
    --enable-portal=builtin \
    --enable-meego=builtin \
    --enable-openconnect=builtin \
    --enable-openvpn=builtin \
    --enable-pacrunner=builtin \
    --enable-ntpd=builtin \
    --with-ntpd=/usr/sbin/ntpd \
    --enable-threads \
    --enable-test \
    --with-systemdunitdir=/%{_lib}/systemd/system

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
mkdir -p %{buildroot}/%{_lib}/systemd/system/network.target.wants
ln -s ../connman.service %{buildroot}/%{_lib}/systemd/system/network.target.wants/connman.service
# << install post


%preun
systemctl stop connman.service

%post
systemctl daemon-reload
systemctl reload-or-try-restart connman.service

%postun
systemctl daemon-reload








%files
%defattr(-,root,root,-)
# >> files
%doc AUTHORS COPYING INSTALL ChangeLog NEWS README
%{_sbindir}/*
%{_libdir}/%{name}/scripts/*
%config %{_sysconfdir}/dbus-1/system.d/*.conf
/%{_lib}/systemd/system/connman.service
/%{_lib}/systemd/system/network.target.wants/connman.service
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%doc AUTHORS COPYING INSTALL
%{_includedir}/%{name}/*.h
%{_libdir}/pkgconfig/*.pc
# << files devel

%files test
%defattr(-,root,root,-)
# >> files test
%{_libdir}/%{name}/test/*
# << files test

