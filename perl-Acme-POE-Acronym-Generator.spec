%define upstream_name    Acme-POE-Acronym-Generator
%define upstream_version 1.18

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Generate random POE acronyms
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Acme/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Math::Random)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
What does POE stand for?" is a common question, and people have expanded
the acronym in several ways.

Acme::POE::Acronym::Generator produces randomly generated expansions of the
POE acronym ( or at your option any other arbitary word ).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.180.0-2mdv2011.0
+ Revision: 654834
- rebuild for updated spec-helper

* Thu Dec 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2011.0
+ Revision: 472984
- import perl-Acme-POE-Acronym-Generator


* Thu Dec 03 2009 cpan2dist 1.18-1mdv
- initial mdv release, generated with cpan2dist
