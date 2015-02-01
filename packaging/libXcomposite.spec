Summary: X Composite Extension library
Name: libXcomposite
Version: 0.4.4
Release: 3
License: MIT
Group: System Environment/Libraries
URL: http://www.x.org

Source0: %{name}-%{version}.tar.gz

BuildRequires: pkgconfig(compositeproto) >= 0.4
BuildRequires: pkgconfig(xfixes) pkgconfig(xext)
BuildRequires: pkgconfig(xorg-macros)
BuildRequires: pkgconfig(xrender) pkgconfig(renderproto)

%description
X Composite Extension library

%package devel
Summary: Development files for %{name}
Group: Development/Libraries
Provides: libxcomposite-devel
Requires: %{name} = %{version}-%{release}
Requires: pkgconfig(xrender)
Requires: pkgconfig(renderproto)

%description devel
X.Org X11 libXcomposite development package

%prep
%setup -q

%build
%reconfigure --disable-static \
		LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed" \
		CFLAGS="${CFLAGS} \
			-Wall -g \
			-D_F_INPUT_REDIRECTION_ \
			"

make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
/usr/share/license/%{name}
#%doc AUTHORS COPYING README ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
#%{_mandir}/man3/X?omposite*.3*
