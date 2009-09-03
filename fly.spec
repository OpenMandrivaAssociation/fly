%define name fly
%define version 2.0.0
%define release %mkrel 8

Summary: Generate GIF on the fly
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://martin.gleeson.com/fly/dist/%{name}-%{version}.tar.bz2
License: Distributable
Group: Graphics
URL: http://martin.gleeson.com/fly/
Buildrequires: gd-devel
Buildrequires: freetype-devel 
BuildRoot: %{_tmppath}/%{name}-buildroot

%description
Fly is a graphic tool to generate gif/png on the fly

%prep

%setup -q

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_bindir
cp fly $RPM_BUILD_ROOT/%_bindir

%clean


%files
%defattr(-,root,root)
%doc README
%doc doc/*
%_bindir/*

