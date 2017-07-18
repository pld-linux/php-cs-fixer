#
# Conditional build:
%bcond_with	tests		# build with tests

%define		php_min_version 5.3.6
%include	/usr/lib/rpm/macros.php
Summary:	PHP Coding Standards Fixer
Name:		php-cs-fixer
Version:	1.13.1
Release:	3
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/FriendsOfPHP/PHP-CS-Fixer/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	9dbb09988ea36876d49601cb8e862939
Source1:	autoload.php
Patch0:		autoload.patch
Patch1:		allow-cache.patch
URL:		http://cs.sensiolabs.org/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.461
%if %{with tests}
BuildRequires:	%{php_name}-cli
BuildRequires:	%{php_name}-ctype
BuildRequires:	%{php_name}-phar
BuildRequires:	%{php_name}-tokenizer
%endif
Requires:	/usr/bin/php
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(phar)
Requires:	php(posix)
Requires:	php(tokenizer)
Requires:	php-sebastian-diff >= 1.1
Requires:	php-symfony2-ClassLoader >= 2.7.7
Requires:	php-symfony2-Console >= 2.3
Requires:	php-symfony2-EventDispatcher >= 2.1
Requires:	php-symfony2-Finder >= 2.1
Requires:	php-symfony2-Process >= 2.3
Requires:	php-symfony2-Stopwatch >= 2.5
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
%setup -qn PHP-CS-Fixer-%{version}
%patch0 -p1
%patch1 -p1

mv Symfony/CS/Resources/phar-stub.php .
cp -p %{SOURCE1} Symfony/CS/autoload.php

%build
ver=$(awk -F"'" '/const VERSION/{print $(NF-1)}' Symfony/CS/Fixer.php)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_data_dir}/Symfony/CS}
cp -a Symfony $RPM_BUILD_ROOT%{php_data_dir}
install -p php-cs-fixer $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{php_data_dir}/Symfony/CS
