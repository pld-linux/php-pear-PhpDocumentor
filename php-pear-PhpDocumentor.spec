# ToDo:
# - solve requires issue (something like patch0, but a bit extended?)
# - maybe PhpDocumentor.ini should go to /etc/php ?
# - Requires: ... pear(@WEB-DIR@/PhpDocumentor/docbuilder/includes/utilities.php) 
# - smarty plugins to /usr/share/pear/Smarty ?
%include	/usr/lib/rpm/macros.php
%define		_class		PhpDocumentor
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of PHP API directly from source
Summary(pl):	%{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze �r�de�
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	0.16
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	200556aaec710a90b4d073fce3547817
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-html_treemenu_includes_fix.patch
URL:		http://pear.php.net/package/PhpDocumentor/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	sed >= 4.0
Requires:	php-pear
Requires:	php-cli
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# dunno, i need this package NOW
%define		_noautoreq	'pear(phpDocumentor/.*)' 'pear(/usr/share/pear/data/PhpDocumentor/docbuilder/includes/utilities.php)' 'pear(HTML_TreeMenu-1.1.2/TreeMenu.php)'

%define		__pear php4 -C -q -d include_path=%{php_pear_dir} -d output_buffering=1 -d memory_limit=16M %{php_pear_dir}/pearcmd.php
%define		_sysconfdir /etc/pear

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

%prep
%setup -q -c

# use pear to install it to ./build
mv package.xml %{_pearname}-%{version}
cd %{_pearname}-%{version}
%{__pear} \
	-d doc_dir=%{_docdir} \
	-d data_dir=%{php_pear_dir}/data \
	install \
	--installroot=../build \
	--offline \
	--nodeps \
	package.xml \

#exit 0
#cd %{_pearname}-%{version}

# undos the sources
find . -type f -print0 | xargs -0 sed -i -e 's,
$,,'

# remove installroot (why it's there?)
grep -rl '\.\./build' ../build | xargs -r sed -i -e 's,\.\./build,,g'

# patch the sources
# include only these to this package and depend on smarty?
#Only in Smarty-2.5.0/libs/plugins: block.strip.php
#Only in Smarty-2.5.0/libs/plugins: function.assign.php
#Only in Smarty-2.5.0/libs/plugins: function.var_dump.php
#Only in Smarty-2.5.0/libs/plugins: modifier.htmlentities.php
#Only in Smarty-2.5.0/libs/plugins: modifier.rawurlencode.php

#%patch0 -p1
#%patch1 -p1

exit 0

# wasn't bundled before. so remove
rm -f Smarty-2.5.0/{BUGS,COPYING.lib,ChangeLog,FAQ,INSTALL,NEWS,README,RELEASE_NOTES,TODO}

# and these. correct if it's wrong
cd Converters/HTML
rm -f \
	Smarty/templates/default/templates/layout.css \
	Smarty/templates/default/templates/style.css \
	frames/templates/DOM/l0l33t/templates/media/bg_left.png \
	frames/templates/DOM/l0l33t/templates/media/minus.gif \
	frames/templates/DOM/l0l33t/templates/media/plus.gif \

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{php_pear_dir}}
cp -a build/%{_bindir}/phpdoc $RPM_BUILD_ROOT%{_bindir}
cp -a build/%{php_pear_dir}/* $RPM_BUILD_ROOT%{php_pear_dir}

cd %{_pearname}-%{version}
#%{__pear} \
#	-d doc_dir=%{_docdir}/%{name}-%{version} \
#	install \
#	--installroot=$RPM_BUILD_ROOT \
#	--offline \
#	--nodeps \
#	--ignore-errors \
#	package.xml
install package.xml $RPM_BUILD_ROOT%{_sysconfdir}/%{_pearname}.xml

# useless
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/tests/PhpDocumentor/Documentation/tests

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{__pear} -q upgrade --register-only --force --offline %{_sysconfdir}/%{_pearname}.xml

%preun
if [ "$1" = 0 ]; then
	%{__pear} -q uninstall --register-only --offline %{_pearname}
fi

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{Authors,ChangeLog,FAQ,INSTALL,PHPLICENSE.txt,README,Release*,poweredbyphpdoc.gif}
%doc %{_pearname}-%{version}/{Documentation,tutorials}
%doc build/usr/bin/scripts
%{_sysconfdir}/*.xml
%attr(755,root,root) %{_bindir}/phpdoc
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*
%{php_pear_dir}/data/%{_class}/*
