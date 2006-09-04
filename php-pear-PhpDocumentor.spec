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
Summary(pl):	%{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze �r�de�
Name:		php-pear-%{_pearname}
Version:	1.3.0
Release:	1
Epoch:		0
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	aed75aaeceb4439ca0534f98e2513683
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-smarty.patch
Patch2:		%{name}-html_treemenu_includes_fix.patch
URL:		http://pear.php.net/package/PhpDocumentor/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	Smarty >= 2.6.10-4
Requires:	php-cli
Requires:	php-common >= 3:4.3.0
Requires:	php-pcre
Requires:	php-pear >= 4:1.0-2.8
Requires:	php-pear-Archive_Tar >= 1.1
Requires:	php-tokenizer
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

%description -l pl
phpDocumentor jest podobnym do JavaDoc samodzielnym narz�dziem do
automatycznego tworzenia dokumentacji napisanym w PHP. W por�wnaniu do
PHPDoc jest du�o szybszy, parsuje wi�kszy zakres plik�w PHP, oraz
umo�liwia dostosowanie do upodoba� u�ytkownika za pomoc� mi�dzy innymi
11 szablon�w HTML, mo�liwo�ci zapisu plik�w w formacie plik�w pomocy
Windows (CHM), PDF czy XML DocBook peardoc2 (u�ywanym przy tworzeniu
dokumentacji do PEAR). Ponadto phpDocumentor mo�e pod�wietla� i ��czy�
kod �r�d�owy za pomoc� PHPXref.

Mo�liwo�ci (kr�tka lista):
- zapis do formatu HTML, PDF (bezpo�rednio), CHM (za pomoc�
  kompilatora plik�w pomocy windows), XML DocBook
- bardzo szybki
- interfejs WWW oraz z linii polece�
- w pe�ni konfigurowalny zapis z u�yciem szablon�w opartych o Smarty
- rozpoznaje dokumentacj� JavaDoc za pomoc� specjalnych znacznik�w
  dostosowanych do PHP 4
- automatyczne ��czenie, diagramy dziedziczenia klas i inteligentne
  przes�anianie
- konfigurowalne pod�wietlanie kodu �r�d�owego z odno�nikami w stylu
  phpxref
- parsuje standardowe pliki README/CHANGELOG/INSTALL/FAQ i do��cza je
  bezpo�rednio do dokumentacji
- generuje list� do zrobienia korzystaj�c ze znacznik�w @todo w kodzie
- generuje r�n� dokumentacj� w zale�no�ci od znacznik�w @access
  private, @internal i {@internal}
- przyk�adowe pliki PHP mog� by� umieszczane bezpo�rednio w
  dokumentacji z pod�wietlaniem sk�adni i po��czeniami phpxref za pomoc�
  znacznika @example
- po��czenia pomi�dzy zewn�trznym podr�cznikiem i dokumentacj� API
  jest mo�liwe na poziomie podsekcji we wszystkich formatach wyj�ciowych
- �atwo rozszerzalny za pomoc� Convertera dla specyficznych potrzeb
  dokumentacji
- pe�na dokumentacja ka�dej z mo�liwo�ci, podr�cznik mo�e by�
  wygenerowany bezpo�rednio z kodu �r�d�owego za pomoc� "phpdoc -c
  makedocs" w dowolnie wybranym formacie
- aktualny podr�cznik zawsze dost�pny pod adresem
  http://www.phpdoc.org/manual.php
- za pomoc� plik�w .ini mo�na kontrolowa� format wyj�cia, mo�na
  generowa� kilka dokument�w naraz

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
