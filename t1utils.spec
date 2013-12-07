Summary: Programs for manipulating PostScript Type 1 fonts
Name: t1utils
Version: 1.37
Release: 5
Source: http://www.lcdf.org/type/%{name}-%{version}.tar.gz
URL: http://www.lcdf.org/type/
Group: Publishing
License: freely modifiable and distributable
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
The t1utils package is a set of programs for manipulating PostScript
Type 1 fonts. It contains programs to change between binary PFB format
(for storage), ASCII PFA format (for printing), a human-readable and
editable ASCII format, and Macintosh resource forks.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc NEWS README
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*




%changelog
* Mon Feb 20 2012 abf
- The release updated by ABF

* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.36-2mdv2011.0
+ Revision: 670659
- mass rebuild

* Sun Aug 15 2010 Emmanuel Andry <eandry@mandriva.org> 1.36-1mdv2011.0
+ Revision: 570140
- New version 1.36

* Tue Mar 02 2010 Emmanuel Andry <eandry@mandriva.org> 1.35-1mdv2010.1
+ Revision: 513658
- New version 1.35
- drop p0 (no longer needed)

* Sat Oct 03 2009 Funda Wang <fwang@mandriva.org> 1.33-2mdv2010.0
+ Revision: 453247
- fix conflicts regarding getline

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 1.33-1mdv2009.1
+ Revision: 333007
- New upstream release

* Fri Dec 19 2008 Oden Eriksson <oeriksson@mandriva.com> 1.32-6mdv2009.1
+ Revision: 316261
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.32-5mdv2009.0
+ Revision: 225606
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.32-4mdv2008.1
+ Revision: 179595
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.32-3mdv2007.0
+ Revision: 114515
- Import t1utils

* Sun Jan 28 2007 Götz Waschk <waschk@mandriva.org> 1.32-3mdv2007.1
- rebuild

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 1.32-3mdk
- Rebuild

* Sat Aug 06 2005 Giuseppe Ghibò <ghibo@mandriva.com> 1.32-2mdk
- Rebuilt.

* Tue Jul 20 2004 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.32-1mdk
- Release: 1.34.


