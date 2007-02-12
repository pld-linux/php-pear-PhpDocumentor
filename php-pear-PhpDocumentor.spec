# TODO:
# - solve requires issue (something like patch0, but a bit extended?)
# - maybe PhpDocumentor.ini should go to /etc/php ?
# - subpackage for -tutorial?
%include	/usr/lib/rpm/macros.php
%define		_class		PhpDocumentor
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of PHP API directly from source
Summary(pl.UTF-8):   %{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze źródeł
Name:		php-pear-%{_pearname}
Version:	1.3.0
%define	_rc RC3
Release:	0.%{_rc}.20
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	d96ccefa7cfce8b0f24216b8f5041ba4
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-html_treemenu_includes_fix.patch
Patch2:		%{name}-smarty.patch
URL:		http://pear.php.net/package/PhpDocumentor/
BuildRequires:	rpm-php-pearprov >= 4.4.2-10.2
Requires:	php-pear >= 4:1.0-2.8
Requires:	php-cli
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_smartyplugindir	%{php_pear_dir}/Smarty/plugins

# don't require %{php_pear_dir}/data files we provide.
# TODO treemenu needs patching (removing from this package)
# pear/PhpDocumentor can optionally use package "pear/XML_Beautifier" (version >= 1.1)
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

%prep
%pear_package_setup

# remove bundled Smarty cache, poldek goes crazy on them (provides/requires payload exceeded 64k)
find -name templates_c | xargs -ri sh -c 'rm -rf {}; mkdir {}'

# patches
#%patch0 -p1
#%patch1 -p1
%patch2 -p1

# remove bundled Smarty. use system one.
mkdir plugins
mv ./%{php_pear_dir}/PhpDocumentor/phpDocumentor/Smarty-*/libs/plugins/\
{block.strip.php,function.{assign,var_dump}.php,modifier.{htmlentities,rawurlencode}.php} plugins
rm -rf ./%{php_pear_dir}/PhpDocumentor/phpDocumentor/Smarty-*
rm -rf ./%{php_pear_dir}/data/PhpDocumentor/phpDocumentor/Smarty-*

# useless
cd ./%{php_pear_dir}
rm -rf tests/PhpDocumentor/Documentation/tests

# and these. correct if it's wrong
cd data/PhpDocumentor/phpDocumentor/Converters/HTML
rm -f \
	Smarty/templates/default/templates/layout.css \
	Smarty/templates/default/templates/style.css \
	frames/templates/DOM/l0l33t/templates/media/bg_left.png \
	frames/templates/DOM/l0l33t/templates/media/minus.gif \
	frames/templates/DOM/l0l33t/templates/media/plus.gif \

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir},%{_smartyplugindir}}
cp -a ./%{_bindir}/phpdoc $RPM_BUILD_ROOT%{_bindir}
%pear_package_install
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
%doc docs/%{_pearname}/{Authors,ChangeLog,FAQ,INSTALL,PHPLICENSE.txt,README,Release*}
%doc docs/%{_pearname}/{Documentation,tutorials}
%{php_pear_dir}/.registry/*.reg
%attr(755,root,root) %{_bindir}/phpdoc

%{php_pear_dir}/%{_class}
%{php_pear_dir}/data/%{_class}

# extra Smarty plugins
%{_smartyplugindir}/*
