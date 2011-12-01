Name:           perl-Crypt-OpenSSL-RSA
Version:        0.25
Release:        10.1%{?dist}
Summary:        Perl interface to OpenSSL for RSA
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Crypt-OpenSSL-RSA/
Source0:        http://www.cpan.org/authors/id/I/IR/IROBERTS/Crypt-OpenSSL-RSA-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  openssl openssl-devel
BuildRequires:  perl(Crypt::OpenSSL::Random) perl(Crypt::OpenSSL::Bignum)
BuildRequires:  perl(Test) perl(ExtUtils::MakeMaker)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       perl(Crypt::OpenSSL::Random)
Requires:	perl(Crypt::OpenSSL::Bignum)

%description
Crypt::OpenSSL::RSA - RSA encoding and decoding, using the openSSL libraries

%prep
%setup -q -n Crypt-OpenSSL-RSA-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/*

%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.25-10.1
- Rebuilt for RHEL 6

* Fri Aug 21 2009 Tomas Mraz <tmraz@redhat.com> - 0.25-10
- rebuilt with new openssl

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.25-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 17 2009 Tomas Mraz <tmraz@redhat.com> - 0.25-7
- rebuild with new openssl

* Wed Jun 18 2008 Wes Hardaker <wjhns174@hardakers.net> - 0.25-6
- Fix bug 451900: force-require the bignum module

* Wed Mar  5 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 0.25-5
- rebuild for new perl

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.25-4
- Autorebuild for GCC 4.3

* Sun Dec 09 2007 Release Engineering <rel-eng at fedoraproject dot org> - 0.25-3
- Rebuild for deps

* Thu Dec  6 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.25-2
- Bump to force rebuild with new openssl lib version

* Thu May 31 2007 Wes Hardaker <wjhns174@hardakers.net> - 0.25-1
- head to upstream 0.25
- doc the new LICENSE file

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.24-4
- Reverse terms in license to match perl rpm exactly

* Mon May 14 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.24-3
- BuildRequire perl(Test) perl(ExtUtils::MakeMaker) perl(Crypt::OpenSSL::Bignum)
- Fixed source code URL

* Tue May  8 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.24-2
- Add BuildRequire openssl-devel
- Don't manually require openssl
- Use vendorarch instead of vendorlib 

* Thu Apr 19 2007  Wes Hardaker <wjhns174@hardakers.net> - 0.24-1
- Initial version
