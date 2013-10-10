#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta-Check
%include	/usr/lib/rpm/macros.perl
Summary:	CPAN::Meta::Check - Verify requirements in a CPAN::Meta object
Name:		perl-CPAN-Meta-Check
Version:	0.007
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	56f71df79cea8d308a552b3eb996deb0
Patch0:		fixdeps.patch
URL:		http://search.cpan.org/dist/CPAN-Meta-Check/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Deep
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module verifies if requirements described in a CPAN::Meta object
are present.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

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
%doc Changes INSTALL README
%{perl_vendorlib}/CPAN/Meta/*.pm
%{_mandir}/man3/*
