# ToDo:
# - solve requires issue (something like patch0, but a bit extended?)
# - simplify creating dirs in %%install
# - maybe PhpDocumentor.ini should go to /etc/php ?

%include	/usr/lib/rpm/macros.php

%define         _class          PhpDocumentor
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of PHP API directly from source
Summary(pl):	%{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze �r�de�
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	0.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	874aa1d7deeff98a272ea204190928fe
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-html_treemenu_includes_fix.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The phpDocumentor tool is a standalone auto-documentor similar to
JavaDoc written in PHP. It differs from PHPDoc in that it is MUCH
faster, parses a much wider range of php files, and comes with many
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
- example php files can be placed directly in documentation with
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

This class has in PEAR status: %{_status}.

%description -l pl
phpDocumentor jest podobnym do JavaDoc samodzielnym narz�dziem do
automatycznego tworzenia dokumentacji napisanym w PHP. W por�wnaniu do
PHPDoc jest du�o szybszy, parsuje wi�kszy zakres plik�w php, oraz
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
- przyk�adowe pliki php mog� by� umieszczane bezpo�rednio w
  dokumentacji z pod�wietlaniem sk�adni i po��czeniami phpxref za
  pomoc� znacznika @example
- po��czenia pomi�dzy zewn�trznym podr�cznikiem i dokumentacj� API
  jest mo�liwe na poziomie podsekcji we wszystkich formatach
  wyj�ciowych
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

%prep
%setup -q -c
%patch0 -p1
%patch1 -p0

%build
cd %{_pearname}-%{version}
# We have php binary in /usr/bin, not in /usr/local/bin
sed 's#/usr/local/bin#/usr/bin#' phpdoc > phpdoc.tmp
mv -f phpdoc.tmp phpdoc

%install
rm -rf $RPM_BUILD_ROOT

# Create directory tree (guess it could be simplified... to be done....)
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{scripts,user}
#install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2/images
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder/{images,includes}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/media/images/earthli
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/templates/default/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CSV/dia2code
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/{HandS,PHP,default}/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/{default,earthli,l0l33t,phpdoc.de,phphtmllib}/{templates/media/{images,lib},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/{templates/media/images,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/{templates/media/{images,lib},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/{templates/media,templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/{default/{templates/media,templates_c},fonts}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/{peardoc2/templates/default/{templates,templates_c},templates/peardoc2/templates}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Smarty-2.5.0/libs/plugins

# Copy files (now I realize how wonderfull is make install...)
install %{_pearname}-%{version}/phpdoc $RPM_BUILD_ROOT%{_bindir}
install %{_pearname}-%{version}/*.{php,ini}  $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
#install %{_pearname}-%{version}/HTML_TreeMenu-1.1.2/TreeMenu.* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2
#install %{_pearname}-%{version}/HTML_TreeMenu-1.1.2/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2/images
install %{_pearname}-%{version}/docbuilder/*.{php,html} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder
install %{_pearname}-%{version}/docbuilder/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder/images
install %{_pearname}-%{version}/docbuilder/includes/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder/includes
install %{_pearname}-%{version}/media/images/earthli/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/media/images/earthli
install %{_pearname}-%{version}/phpDocumentor/*.{inc,php} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor

# Gosh... There are soooo many subdirectories in Converters/
install %{_pearname}-%{version}/phpDocumentor/Converters/CHM/default/*.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default
install %{_pearname}-%{version}/phpDocumentor/Converters/CHM/default/templates/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/templates/default
install %{_pearname}-%{version}/phpDocumentor/Converters/CHM/default/templates/default/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/templates/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/CHM/default/templates/default/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/templates/default/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/CHM/default/templates/default/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/templates/default/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/CSV/dia2code/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CSV/dia2code

#install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/ $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/*.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/HandS
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/PHP
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/default
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/default/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/*.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/templates_c

install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/default/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/default/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/default/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/earthli/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates_c/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media/*.css $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media/images
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media/lib/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates/media/lib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/*.{inc,php} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/templates/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/default
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/templates/default/templates/*.tpl $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/templates/default/templates/media/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/default/templates/media
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/templates/default/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/default/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/PDF/default/templates/fonts/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/templates/fonts
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/*.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/peardoc2/*.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/peardoc2
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default/*.ini $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default/templates/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default/templates
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default/templates_c/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/peardoc2/templates/default/templates_c
install %{_pearname}-%{version}/phpDocumentor/Converters/XML/DocBook/templates/peardoc2/templates/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/templates/peardoc2/templates
install %{_pearname}-%{version}/phpDocumentor/Smarty-2.5.0/libs/*.{php,tpl} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Smarty-2.5.0/libs
install %{_pearname}-%{version}/phpDocumentor/Smarty-2.5.0/libs/plugins/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Smarty-2.5.0/libs/plugins
install %{_pearname}-%{version}/scripts/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/scripts/
install %{_pearname}-%{version}/user/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/user/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{Authors,ChangeLog,FAQ,INSTALL,LICENSE,PHPLICENSE.txt,README,Release*,poweredbyphpdoc.gif}
%doc %{_pearname}-%{version}/{Documentation,tutorials}
%attr(755,root,root) %{_bindir}/phpdoc
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*
