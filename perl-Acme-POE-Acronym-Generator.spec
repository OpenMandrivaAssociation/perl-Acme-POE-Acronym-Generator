%define upstream_name    Acme-POE-Acronym-Generator
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

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
