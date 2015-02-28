#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	JavaScript
%define		pnam	Minifier
%include	/usr/lib/rpm/macros.perl
Summary:	JavaScript::Minifier - Perl extension for minifying JavaScript code
Name:		perl-JavaScript-Minifier
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/JavaScript/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	07dadb99434c749eb8960d075244aea3
URL:		http://search.cpan.org/dist/JavaScript-Minifier/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module removes unnecessary whitespace from JavaScript code. The
primary requirement developing this module is to not break working
code: if working JavaScript is in input then working JavaScript is
output. It is ok if the input has missing semi-colons, snips like '++
+' or '12 .toString()', for example. Internet Explorer conditional
comments are copied to the output but the code inside these comments
will not be minified.

The ECMAScript specifications allow for many different whitespace
characters: space, horizontal tab, vertical tab, new line, carriage
return, form feed, and paragraph separator. This module understands
all of these as whitespace except for vertical tab and paragraph
separator. These two types of whitespace are not minimized.

For static JavaScript files, it is recommended that you minify during
the build stage of web deployment. If you minify on-the-fly then it
might be a good idea to cache the minified file. Minifying static
files on-the-fly repeatedly is wasteful.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/JavaScript/*.pm
%{_mandir}/man3/*
