
Name:       libxcomposite
Summary:    X.Org X11 libXcomposite runtime library
Version:    0.4.3
Release:    2.4
Group:      System/Libraries
License:    MIT/X11
URL:        http://www.x.org
Source0:    http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(fixesproto)
BuildRequires:  pkgconfig(xorg-macros)


%description
X Composite Library


%package devel
Summary:    X.Org X11 libXcomposite development package
Group:      System/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   xorg-x11-filesystem

%description devel
Development files for libxcomposite


%prep
%setup -q -n %{name}-%{version}


%build
export LDFLAGS+=" -Wl,--hash-style=both -Wl,--as-needed"
%reconfigure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install




%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0


%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/X11
%dir %{_includedir}/X11/extensions
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%doc %{_mandir}/man3/X?omposite*.3*

