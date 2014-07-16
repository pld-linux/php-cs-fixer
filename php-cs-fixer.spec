# TODO
# - unbundle phar, use system libs, etc
%define		githash	3cef8c3
%define		rel		0.5
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	PHP Coding Standards Fixer
Name:		php-cs-fixer
Version:	0.3.0
Release:	0.%{githash}.%{rel}
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://cs.sensiolabs.org/get/%{name}.phar
# Source0-md5:	501733ff21110855b7edb44bda998800
URL:		http://cs.sensiolabs.org/
Requires:	/usr/bin/php
Requires:	php(core) >= %{php_min_version}
Requires:	php(phar)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PHP Coding Standards Fixer tool fixes most issues in your code
when you want to follow the PHP coding standards as defined in the
PSR-1 and PSR-2 documents.

If you are already using PHP_CodeSniffer to identify coding standards
problems in your code, you know that fixing them by hand is tedious,
especially on large projects. This tool does the job for you.

%prep
%setup -qcT
cp -p %{SOURCE0} .

# breaks signature:
#%{__sed} -i -e '1 s,#!.*php,#!/usr/bin/php,' php-cs-fixer.phar

%build
# PHP CS Fixer version 0.3-DEV by Fabien Potencier (3cef8c3)
long_version=$(php php-cs-fixer.phar --version)
ver=$(echo "${long_version}" | awk '$4 == "version" {v=$5; sub(/-DEV/, ".0", v); print v}')
test "$ver" = %{version}

githash=$(echo "${long_version##* }" | tr -d '()')
test "$githash" = %{githash}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p php-cs-fixer.phar $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
