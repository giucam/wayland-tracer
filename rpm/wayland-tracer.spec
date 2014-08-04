Name:       wayland-tracer
Summary:    Wayland tracer
Version:    0.0.1
Release:    1
Group:      System/Applications
License:    MIT
URL:        https://github.com/dboyan/wayland-tracer
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: wayland

%description
Wayland tracer

%prep
%setup -q -n %{name}-%{version}

%build

%reconfigure

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
%{_bindir}/wayland-tracer
%{_datadir}/man/man1/wayland-tracer.1.gz
