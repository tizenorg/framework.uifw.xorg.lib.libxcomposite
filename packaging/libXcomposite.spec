Name:           libXcomposite
Version:        0.4.4
Release:        3
License:        MIT
Summary:        X Composite Extension library
Url:            http://www.x.org
Group:          Graphics/X Window System

Source:         %{name}-%{version}.tar.bz2
Source1001: 	libXcomposite.manifest

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
cp %{SOURCE1001} .

%build
%reconfigure --disable-static \
		LDFLAGS="${LDFLAGS} -Wl,--hash-style=both -Wl,--as-needed" \
		CFLAGS="${CFLAGS} \
			-Wall -g \
			-D_F_INPUT_REDIRECTION_ \
			"

make %{?jobs:-j%jobs}

%install
mkdir -p %{buildroot}/usr/share/license
cp -af COPYING %{buildroot}/usr/share/license/%{name}
%make_install

%remove_docs

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
/usr/share/license/%{name}
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
