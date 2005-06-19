# ToDo:
# - solve requires issue (something like patch0, but a bit extended?)
# - maybe PhpDocumentor.ini should go to /etc/php ?
# - Requires: ... pear(@WEB-DIR@/PhpDocumentor/docbuilder/includes/utilities.php) 
# - smarty plugins to /usr/share/pear/Smarty ?
%include	/usr/lib/rpm/macros.php
%define		_class		PhpDocumentor
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of PHP API directly from source
Summary(pl):	%{_pearname} - automatyczne tworzenie dokumentacji API PHP prosto ze ¼róde³
Name:		php-pear-%{_pearname}
Version:	1.3.0
%define	_rc RC3
Release:	0.%{_rc}.4
License:	PHP 3.00
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_rc}.tgz
# Source0-md5:	d96ccefa7cfce8b0f24216b8f5041ba4
Patch0:		%{name}-includes_fix.patch
Patch1:		%{name}-html_treemenu_includes_fix.patch
URL:		http://pear.php.net/package/PhpDocumentor/
BuildRequires:	php-pear-PEAR >= 1.4.0-0.a11.5
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
BuildRequires:	sed >= 4.0
Requires(post):		php-pear-PEAR
Requires(preun):	php-pear-PEAR
Requires:	php-pear >= 4:1.0-2.8
Requires:	php-cli
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# dunno, i need this package NOW
#%define		_noautoreq	'pear(phpDocumentor/.*)' 'pear(/usr/share/pear/data/PhpDocumentor/docbuilder/includes/utilities.php)' 'pear(HTML_TreeMenu-1.1.2/TreeMenu.php)'

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
phpDocumentor jest podobnym do JavaDoc samodzielnym narzêdziem do
automatycznego tworzenia dokumentacji napisanym w PHP. W porównaniu do
PHPDoc jest du¿o szybszy, parsuje wiêkszy zakres plików PHP, oraz
umo¿liwia dostosowanie do upodobañ u¿ytkownika za pomoc± miêdzy innymi
11 szablonów HTML, mo¿liwo¶ci zapisu plików w formacie plików pomocy
Windows (CHM), PDF czy XML DocBook peardoc2 (u¿ywanym przy tworzeniu
dokumentacji do PEAR). Ponadto phpDocumentor mo¿e pod¶wietlaæ i ³±czyæ
kod ¼ród³owy za pomoc± PHPXref.

Mo¿liwo¶ci (krótka lista):
- zapis do formatu HTML, PDF (bezpo¶rednio), CHM (za pomoc±
  kompilatora plików pomocy windows), XML DocBook
- bardzo szybki
- interfejs WWW oraz z linii poleceñ
- w pe³ni konfigurowalny zapis z u¿yciem szablonów opartych o Smarty
- rozpoznaje dokumentacjê JavaDoc za pomoc± specjalnych znaczników
  dostosowanych do PHP 4
- automatyczne ³±czenie, diagramy dziedziczenia klas i inteligentne
  przes³anianie
- konfigurowalne pod¶wietlanie kodu ¼ród³owego z odno¶nikami w stylu
  phpxref
- parsuje standardowe pliki README/CHANGELOG/INSTALL/FAQ i do³±cza je
  bezpo¶rednio do dokumentacji
- generuje listê do zrobienia korzystaj±c ze znaczników @todo w kodzie
- generuje ró¿n± dokumentacjê w zale¿no¶ci od znaczników @access
  private, @internal i {@internal}
- przyk³adowe pliki PHP mog± byæ umieszczane bezpo¶rednio w
  dokumentacji z pod¶wietlaniem sk³adni i po³±czeniami phpxref za pomoc±
  znacznika @example
- po³±czenia pomiêdzy zewnêtrznym podrêcznikiem i dokumentacj± API
  jest mo¿liwe na poziomie podsekcji we wszystkich formatach wyj¶ciowych
- ³atwo rozszerzalny za pomoc± Convertera dla specyficznych potrzeb
  dokumentacji
- pe³na dokumentacja ka¿dej z mo¿liwo¶ci, podrêcznik mo¿e byæ
  wygenerowany bezpo¶rednio z kodu ¼ród³owego za pomoc± "phpdoc -c
  makedocs" w dowolnie wybranym formacie
- aktualny podrêcznik zawsze dostêpny pod adresem
  http://www.phpdoc.org/manual.php
- za pomoc± plików .ini mo¿na kontrolowaæ format wyj¶cia, mo¿na
  generowaæ kilka dokumentów naraz

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

# use pear to install it to ../build
mv package.xml %{_pearname}-%{version}%{_rc}
cd %{_pearname}-%{version}%{_rc}
pear \
	-d doc_dir=%{_docdir} \
	-d data_dir=%{php_pear_dir}/data \
	install \
	--installroot=../build \
	--offline \
	--nodeps \
	package.xml \

cd ../build

# undos the sources
find . -type f -print0 | xargs -0 sed -i -e 's,
$,,'

# jesus, remove the Smarty cache, poldek goes crazy on them
find -name templates_c | xargs -ri sh -c 'rm -rf {}; mkdir {}'

# patches
#%patch0 -p1
#%patch1 -p1

# remove installroot (why it's there?)
grep -rl '\.\./build' ../build | xargs -r sed -i -e 's,\.\./build,,g'

# useless
cd .%{php_pear_dir}
rm -rf tests/PhpDocumentor/Documentation/tests

# patch the sources
# include only these to this package and depend on smarty?
#Only in Smarty-2.5.0/libs/plugins: block.strip.php
#Only in Smarty-2.5.0/libs/plugins: function.assign.php
#Only in Smarty-2.5.0/libs/plugins: function.var_dump.php
#Only in Smarty-2.5.0/libs/plugins: modifier.htmlentities.php
#Only in Smarty-2.5.0/libs/plugins: modifier.rawurlencode.php

# wasn't bundled before. so remove
rm -f PhpDocumentor/phpDocumentor/Smarty-2.5.0/{BUGS,COPYING.lib,ChangeLog,FAQ,INSTALL,NEWS,README,RELEASE_NOTES,TODO}

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

install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}}
cp -a build/%{_bindir}/phpdoc $RPM_BUILD_ROOT%{_bindir}
cp -a build/%{php_pear_dir}/* $RPM_BUILD_ROOT%{php_pear_dir}

cd %{_pearname}-%{version}%{_rc}
pear -q install \
	--register-only --force --offline \
	--installroot=$RPM_BUILD_ROOT package.xml

# pear registry files
rm -rf $RPM_BUILD_ROOT%{php_pear_dir}/.{channels,dep*,filemap,lock}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_rc}/{Authors,ChangeLog,FAQ,INSTALL,PHPLICENSE.txt,README,Release*,poweredbyphpdoc.gif}
%doc %{_pearname}-%{version}%{_rc}/{Documentation,tutorials}
%doc build/usr/bin/scripts
%attr(755,root,root) %{_bindir}/phpdoc

%{php_pear_dir}/%{_class}
%{php_pear_dir}/data/%{_class}

%{php_pear_dir}/.registry/*.reg
