# TODO:
# - solve requires issue (something like patch0, but a bit extended?)
# - maybe PhpDocumentor.ini should go to /etc/php ?
# - subpackage for -tutorial?
# - subpackage for -cli?
# - subpackage docBuilder for web interface in %{php_pear_dir}/data/%{_pearname}
# - treemenu needs patching (removing from this package)
%include	/usr/lib/rpm/macros.php
%define		_class		PhpDocumentor
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of PHP API directly from source
Summary(pl.UTF-8):   %{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze źródeł
Name:		php-pear-%{_pearname}
Version:	1.3.1
Release:	2
Epoch:		0
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	4209e449b2b94180f3bf6bc74cf3031f
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-smarty.patch
Patch2:		%{name}-html_treemenu_includes_fix.patch
URL:		http://pear.php.net/package/PhpDocumentor/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	Smarty >= 2.6.10-4
Requires:	php(pcre)
Requires:	php(tokenizer)
Requires:	php-cli
Requires:	php-common >= 3:4.3.0
Requires:	php-pear >= 4:1.0-2.8
Requires:	php-pear-Archive_Tar >= 1.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartyplugindir	%{_datadir}/php/Smarty/plugins

# exclude optional dependencies
# don't require %{php_pear_dir}/data files we provide.
%define		_noautoreq	'pear(phpDocumentor/.*)' 'pear(%{php_pear_dir}/data/.*)' 'pear(XML/Beautifier/.*)' 'pear(HTML_TreeMenu-1.1.2/TreeMenu.php)'

%description
The phpDocumentor tool is a standalone auto-documentor similar to
JavaDoc written in PHP. It differs from PHPDoc in that it is MUCH
faster, parses a much wider range of PHP files, and comes with many
customizations including 11 HTML templates, windows help file CHM
output, PDF output, and XML DocBook peardoc2 output for use with
documenting PEAR. In addition, it can do PHPXref source code
highlighting and linking.

Features (short list):
- output in HTML, PDF (directly), CHM (with windows help compiler),
  XML DocBook
- very fast
- web and command-line interface
- fully customizable output with Smarty-based templates
- recognizes JavaDoc-style documentation with special tags customized
  for PHP 4
- automatic linking, class inheritance diagrams and intelligent
  override
- customizable source code highlighting, with phpxref-style
  cross-referencing
- parses standard README/CHANGELOG/INSTALL/FAQ files and includes them
  directly in documentation
- generates a todo list from @todo tags in source
- generates multiple documentation sets based on @access private,
  @internal and {@internal} tags
- example PHP files can be placed directly in documentation with
  highlighting and phpxref linking using the @example tag
- linking between external manual and API documentation is possible at
  the sub-section level in all output formats
- easily extended for specific documentation needs with Converter
- full documentation of every feature, manual can be generated
  directly from the source code with "phpdoc -c makedocs" in any format
  desired.
- current manual always available at http://www.phpdoc.org/manual.php
- user .ini files can be used to control output, multiple outputs can
  be generated at once

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
phpDocumentor jest podobnym do JavaDoc samodzielnym narzędziem do
automatycznego tworzenia dokumentacji napisanym w PHP. W porównaniu do
PHPDoc jest dużo szybszy, parsuje większy zakres plików PHP, oraz
umożliwia dostosowanie do upodobań użytkownika za pomocą między innymi
11 szablonów HTML, możliwości zapisu plików w formacie plików pomocy
Windows (CHM), PDF czy XML DocBook peardoc2 (używanym przy tworzeniu
dokumentacji do PEAR). Ponadto phpDocumentor może podświetlać i łączyć
kod źródłowy za pomocą PHPXref.

Możliwości (krótka lista):
- zapis do formatu HTML, PDF (bezpośrednio), CHM (za pomocą
  kompilatora plików pomocy windows), XML DocBook
- bardzo szybki
- interfejs WWW oraz z linii poleceń
- w pełni konfigurowalny zapis z użyciem szablonów opartych o Smarty
- rozpoznaje dokumentację JavaDoc za pomocą specjalnych znaczników
  dostosowanych do PHP 4
- automatyczne łączenie, diagramy dziedziczenia klas i inteligentne
  przesłanianie
- konfigurowalne podświetlanie kodu źródłowego z odnośnikami w stylu
  phpxref
- parsuje standardowe pliki README/CHANGELOG/INSTALL/FAQ i dołącza je
  bezpośrednio do dokumentacji
- generuje listę do zrobienia korzystając ze znaczników @todo w kodzie
- generuje różną dokumentację w zależności od znaczników @access
  private, @internal i {@internal}
- przykładowe pliki PHP mogą być umieszczane bezpośrednio w
  dokumentacji z podświetlaniem składni i połączeniami phpxref za pomocą
  znacznika @example
- połączenia pomiędzy zewnętrznym podręcznikiem i dokumentacją API
  jest możliwe na poziomie podsekcji we wszystkich formatach wyjściowych
- łatwo rozszerzalny za pomocą Convertera dla specyficznych potrzeb
  dokumentacji
- pełna dokumentacja każdej z możliwości, podręcznik może być
  wygenerowany bezpośrednio z kodu źródłowego za pomocą "phpdoc -c
  makedocs" w dowolnie wybranym formacie
- aktualny podręcznik zawsze dostępny pod adresem
  http://www.phpdoc.org/manual.php
- za pomocą plików .ini można kontrolować format wyjścia, można
  generować kilka dokumentów naraz

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):   Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
%patch0 -p1
%patch1 -p1

rm -f docs/%{_pearname}/PHPLICENSE # PHP License

# remove bundled Smarty. use system one.
mkdir plugins
mv ./%{php_pear_dir}/PhpDocumentor/phpDocumentor/Smarty-*/libs/plugins/\
{block.strip.php,function.{assign,var_dump}.php,modifier.{htmlentities,rawurlencode}.php} plugins
rm -rf ./%{php_pear_dir}/PhpDocumentor/phpDocumentor/Smarty-*
rm -rf ./%{php_pear_dir}/data/PhpDocumentor/phpDocumentor/Smarty-*

# packaging corrections. we want sample scripts in doc
install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/scripts docs/%{_pearname}
mv ./%{_bindir}/scripts/* docs/%{_pearname}/scripts

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir},%{_smartyplugindir}}
%pear_package_install
cp -a ./%{_bindir}/phpdoc $RPM_BUILD_ROOT%{_bindir}
cp -a plugins/* $RPM_BUILD_ROOT%{_smartyplugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpdoc

%{php_pear_dir}/%{_class}
%{php_pear_dir}/data/%{_class}

# extra Smarty plugins
%{_smartyplugindir}/*

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
