Summary: Programs for manipulating PostScript Type 1 fonts
Name: t1utils
Version: 1.32
Release: %mkrel 3
Source: http://www.lcdf.org/type/%{name}-%{version}.tar.bz2
URL: http://www.lcdf.org/type/
Group: Publishing
License: freely modifiable and distributable

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
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README
%attr(0755,root,root) %{_bindir}/*
%attr(0644,root,root) %{_mandir}/man1/*


