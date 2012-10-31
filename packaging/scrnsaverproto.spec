Name:     scrnsaverproto
Summary:  X.Org X11 Protocol scrnsaverproto
Version:  1.2.2
Release:  1
Group:    Development/System
License:  MIT
URL:      http://www.x.org
Source0:  %{name}-%{version}.tar.bz2

BuildRequires: pkgconfig
BuildRequires: pkgconfig(xorg-macros)

%description
Description: %{summary}

%prep
%setup -q

%build

./autogen.sh
%reconfigure --disable-static \
             --libdir=%{_datadir} \
             --without-xmlto

# Call make instruction with smp support
make %{?jobs:-j%jobs}

%install
%make_install

%remove_docs


%files
%defattr(-,root,root,-)
%{_includedir}/X11/extensions/*.h
%{_datadir}/pkgconfig/*.pc
