# ToDo:
# - solve requires issue (something like patch0, but a bit extended?)
# - simplify creating dirs in %%install
# - fix pl description (especially those marked with [FIXME])
# - maybe PhpDocumentor.ini should go to /etc/php ?

%include	/usr/lib/rpm/macros.php

%define         _class          PhpDocumentor
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - provides automatic documenting of php api directly from source
Summary(pl):	%{_pearname} - automatyczne tworzenie dokumentacji api php prosto ze ¼róde³
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	0.1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	874aa1d7deeff98a272ea204190928fe
Patch0:		%{name}-includes_fix.patch
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
phpDocumentor jest podobnym do JavaDoc samodzielnym narzêdziem do
automatycznego tworzenia dokumentacji. W porównaniu do PHPDoc jest
du¿o szybszy, parsuje wiêkszy zakres plików php, oraz umo¿liwia
dostosowanie do upodobañ u¿ytkownika za pomoc± miêdzy innymi 11
szablonów HTML, formacie plików pomocy Windows (CHM), PDF, czy XML
DocBook peardoc2 u¿ywanego przy tworzeniu dokumentacji do PEAR.
Dodatkowo, phpDocumentor mo¿e pod¶wietliæ kod ¼ród³owy i ³±czenia
za pomoc± PHPXref. [FIXME]

Cechy (krótka lista):
- zapis do formatu HTML, PDF (bezpo¶rednio), CHM (za pomoc±
  kompilatora plików pomocy windows), XML DocBook
- bardzo szybki
- interfejs www oraz CLI
- w pe³ni konfigurowywalny zapis za pomoc± szablonów oparty o Smarty
- rozpoznaje dokumentacjê JavaDoc za pomoc± specjalnych tagów
  dostosowanych do PHP 4 [FIXME]
- automatyczne linkowanie, diagramy dziedziczenia klas i (...) [FIXME]
- konfigurowywalne pod¶wietlanie kodu ¼ród³owego z cross-referencj±
  phpxref [FIXME]
- parsuje standardowe pliki README/CHANGELOG/INSTALL/FAQ i do³±cza je
  bezpo¶rednio do dokumentacji
- generuje listê do zrobienia krozystaj±c z tagów @todo w ¼ród³ach
- generuje ró¿n± dokumetnacjê w zale¿no¶ci od tagów @access private,
  @internal i {@internal}
- przyk³adowe pliki php mog± byæ umieszczane bezpo¶rednio w
  dokumentacji z podswietlaniem sk³adni i po³±czeniami phpxref za pomoc±
  taga @example
- po³±czenia pomiêdzy zewnêtrznym podrêcznikiem i dokumentacj± API
  jest mo¿liwe na poziomie podsekcji w ka¿dym rodzaju formatu
  wyj¶ciowego
- ³atwo rozszerzalne za pomoc± Convertera dla specyficznych potrzeb
  dokumentacji
- pe³na dokumentacja ka¿dej cechy, podrêcznik mo¿e byæ wygenerowany
  bezpo¶rednio z kodu ¼ród³owego za pomoc± "phpdoc -c makedocs" w
  dowolnie wybranym formacie
- aktualny podrêcznik zawsze dostêpny pod adresem
  http://www.phpdoc.org/manual.php
- za pomoc± plików .ini mo¿na kontrolowaæ format wyj¶cia,jak równie¿
  mo¿liwe jest generowanie kilku rodzajów wyj¶æ jednocze¶nie. [FIXME]

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c
%patch0 -p1

%build
cd %{_pearname}-%{version}
# We have php binary in /usr/bin, not in /usr/local/bin
sed 's#/usr/local/bin#/usr/bin#' phpdoc > phpdoc.tmp
mv -f phpdoc.tmp phpdoc

%install
rm -rf $RPM_BUILD_ROOT

# Create directory tree (guess it could be simplified... to be done....)
install -d $RPM_BUILD_ROOT{%{_bindir},%{php_pear_dir}/{,%{_class}}}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{HTML_TreeMenu-1.1.2,docbuilder,media,phpDocumentor,scripts,user}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2/images
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder/{images,includes}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/media/images/{,earthli}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/{Converters,Smarty-2.5.0}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/{CHM,CSV,HTML,PDF,XML}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CHM/default/{,templates/{,default/{,templates/{,media},templates_c}}}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/CSV/dia2code/
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/{Smarty,frames}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/{,HandS,PHP,deafault}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/HandS/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/PHP/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/Smarty/templates/default/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/{,DOM,default,earthli,l0l33t,phpdoc.de,phpedit,phphtmllib}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/default/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/earthli/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/l0l33t/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phpdoc.de/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/DOM/phphtmllib/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/default/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/earthli/{templates/{,media/{,images}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/l0l33t/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpdoc.de/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phpedit/{templates/{,media/{,images,lib}},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/HTML/frames/templates/phphtmllib/{templates/{,media},templates_c}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/PDF/default/{,templates/{,default/{,templates/{,media},templates_c},fonts}}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Converters/XML/DocBook/{,peardoc2/{,templates/{,default/{,templates,templates_c}}},templates/{,peardoc2/{,templates}}}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/phpDocumentor/Smarty-2.5.0/libs/{,plugins}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/scripts
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/user

# Copy files (now I realize how wonderfull is make install...)
install %{_pearname}-%{version}/phpdoc $RPM_BUILD_ROOT%{_bindir}
install %{_pearname}-%{version}/*.{php,ini}  $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/HTML_TreeMenu-1.1.2/TreeMenu.* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2/
install %{_pearname}-%{version}/HTML_TreeMenu-1.1.2/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/HTML_TreeMenu-1.1.2/images/
install %{_pearname}-%{version}/docbuilder/*.{php,html} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/docbuilder/
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
