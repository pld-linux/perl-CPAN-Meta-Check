#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CPAN
%define		pnam	Meta-Check
Summary:	CPAN::Meta::Check - Verify requirements in a CPAN::Meta object
Summary(pl.UTF-8):	CPAN::Meta::Check - sprawdzanie wymagań w obiekcie CPAN::Meta
Name:		perl-CPAN-Meta-Check
Version:	0.014
Release:	1
# same as perl 5
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CPAN/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ccd4448a7b08e1e3ef6f475030b282c9
Patch0:		fixdeps.patch
URL:		https://metacpan.org/release/CPAN-Meta-Check
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.30
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-CPAN-Meta >= 2.132830
BuildRequires:	perl-CPAN-Meta-Requirements >= 2.121
BuildRequires:	perl-Module-Metadata >= 1.000023
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Simple >= 0.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module verifies if requirements described in a CPAN::Meta object
are present.

%description -l pl.UTF-8
Ten moduł weryfikuje, czy zależności (wymagane moduły) opisane w
obiekcie CPAN::Meta są spełnione.

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
%doc Changes README
%{perl_vendorlib}/CPAN/Meta/Check.pm
%{_mandir}/man3/CPAN::Meta::Check.3pm*
