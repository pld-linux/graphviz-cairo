Summary:	Cairo renderer plugin for graphviz
Summary(pl):	Wtyczka renderuj±ca Cairo dla graphviza
Name:		graphviz-cairo
Version:	2.4
Release:	1
License:	CPL v1.0
Group:		X11/Applications/Graphics
Source0:	http://www.graphviz.org/pub/graphviz/ARCHIVE/%{name}-%{version}.tar.gz
# Source0-md5:	62c363e278a2854a50f3ae12ae3655c8
URL:		http://www.graphviz.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	cairo-devel >= 0.5.1
BUildRequires:	graphviz-devel >= 2.4
BuildRequires:	gtk+2-devel >= 2:2.7.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A renderer plugin for graphviz that uses cairo and provides output
formats such as PNG, X11.

%description -l pl
Wtyczka renderuj±ca dla graphviza u¿ywaj±ca cairo i udostêpniaj±ca
formaty wyj¶ciowe takie jak PNG, X11.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-x
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -V > /dev/null 2>&1

%postun
umask 022
[ ! -x %{_bindir}/dot ] || %{_bindir}/dot -V > /dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/graphviz/*.so*
