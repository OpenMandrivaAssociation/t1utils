Summary: Programs for manipulating PostScript Type 1 fonts
Name: t1utils
Version: 1.33
Release: %mkrel 2
Source: http://www.lcdf.org/type/%{name}-%{version}.tar.bz2
Patch0: t1utils-1.33-fix-getline.patch
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
%patch0 -p0

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


