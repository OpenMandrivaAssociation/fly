%define name fly
%define version 2.0.0
%define release 10

Summary: Generate GIF on the fly
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://martin.gleeson.com/fly/dist/%{name}-%{version}.tar.bz2
License: Distributable
Group: Graphics
URL: https://martin.gleeson.com/fly/
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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-9mdv2011.0
+ Revision: 610716
- rebuild

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 2.0.0-8mdv2010.0
+ Revision: 428808
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-7mdv2009.0
+ Revision: 245242
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 2.0.0-5mdv2008.1
+ Revision: 140730
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import fly


* Fri Oct 07 2005 Nicolas Lécureuil <neoclust@mandriva.org> 2.0.0-5mdk
- Fix BuildRequires
- %%mkrel

* Thu Jun 03 2004 Michael Scherer <misc@mandrake.org> 2.0.0-4mdk 
- rebuild for new libintl
- simplify BuildRequires
- rpmbuildupdate aware

* Tue Apr 29 2003 Lenny Cartier <lenny@mandrakesoft.com 2.0.0-3mdk
- adjust buildrequires

* Sat Feb 01 2003 Lenny Cartier <lenny@mandrakesoft.com 2.0.0-2mdk
- rebuild

* Mon Aug 26 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.0.0-1mdk
- 2.0.0
- from Laurent Domisse <domisse@w3perl.com> :
	- First RPM release


# end of file
