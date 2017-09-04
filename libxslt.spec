#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x15588B26596BEA5D (Daniel.Veillard@w3.org)
#
Name     : libxslt
Version  : 1.1.30
Release  : 27
URL      : http://xmlsoft.org/sources/libxslt-1.1.30.tar.gz
Source0  : http://xmlsoft.org/sources/libxslt-1.1.30.tar.gz
Source99 : http://xmlsoft.org/sources/libxslt-1.1.30.tar.gz.asc
Summary  : Library providing the GNOME XSLT engine
Group    : Development/Tools
License  : MIT
Requires: libxslt-bin
Requires: libxslt-lib
Requires: libxslt-python
Requires: libxslt-data
Requires: libxslt-doc
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-python
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python-dev
BuildRequires : xz-dev
BuildRequires : zlib-dev
Patch1: 0004-Make-generate-id-deterministic.patch

%description
This C library allows to transform XML files into other XML files
(or HTML, text, ...) using the standard XSLT stylesheet transformation
mechanism. To use it you need to have a version of libxml2 >= 2.6.27
installed. The xsltproc command is a command line interface to the XSLT engine

%package bin
Summary: bin components for the libxslt package.
Group: Binaries
Requires: libxslt-data

%description bin
bin components for the libxslt package.


%package data
Summary: data components for the libxslt package.
Group: Data

%description data
data components for the libxslt package.


%package dev
Summary: dev components for the libxslt package.
Group: Development
Requires: libxslt-lib
Requires: libxslt-bin
Requires: libxslt-data
Provides: libxslt-devel

%description dev
dev components for the libxslt package.


%package doc
Summary: doc components for the libxslt package.
Group: Documentation

%description doc
doc components for the libxslt package.


%package lib
Summary: lib components for the libxslt package.
Group: Libraries
Requires: libxslt-data

%description lib
lib components for the libxslt package.


%package python
Summary: python components for the libxslt package.
Group: Default

%description python
python components for the libxslt package.


%prep
%setup -q -n libxslt-1.1.30
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1504538298
export CFLAGS="$CFLAGS -fstack-protector-strong "
export FCFLAGS="$CFLAGS -fstack-protector-strong "
export FFLAGS="$CFLAGS -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1504538298
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/xsltConf.sh

%files bin
%defattr(-,root,root,-)
/usr/bin/xslt-config
/usr/bin/xsltproc

%files data
%defattr(-,root,root,-)
/usr/share/doc/libxslt-python-1.1.30/TODO
/usr/share/doc/libxslt-python-1.1.30/examples/basic.py
/usr/share/doc/libxslt-python-1.1.30/examples/basic.pyc
/usr/share/doc/libxslt-python-1.1.30/examples/basic.pyo
/usr/share/doc/libxslt-python-1.1.30/examples/exslt.py
/usr/share/doc/libxslt-python-1.1.30/examples/exslt.pyc
/usr/share/doc/libxslt-python-1.1.30/examples/exslt.pyo
/usr/share/doc/libxslt-python-1.1.30/examples/extelem.py
/usr/share/doc/libxslt-python-1.1.30/examples/extelem.pyc
/usr/share/doc/libxslt-python-1.1.30/examples/extelem.pyo
/usr/share/doc/libxslt-python-1.1.30/examples/extfunc.py
/usr/share/doc/libxslt-python-1.1.30/examples/extfunc.pyc
/usr/share/doc/libxslt-python-1.1.30/examples/extfunc.pyo
/usr/share/doc/libxslt-python-1.1.30/examples/pyxsltproc.py
/usr/share/doc/libxslt-python-1.1.30/examples/pyxsltproc.pyc
/usr/share/doc/libxslt-python-1.1.30/examples/pyxsltproc.pyo
/usr/share/doc/libxslt-python-1.1.30/examples/test.xml
/usr/share/doc/libxslt-python-1.1.30/examples/test.xsl

%files dev
%defattr(-,root,root,-)
/usr/include/libexslt/exslt.h
/usr/include/libexslt/exsltconfig.h
/usr/include/libexslt/exsltexports.h
/usr/include/libxslt/attributes.h
/usr/include/libxslt/documents.h
/usr/include/libxslt/extensions.h
/usr/include/libxslt/extra.h
/usr/include/libxslt/functions.h
/usr/include/libxslt/imports.h
/usr/include/libxslt/keys.h
/usr/include/libxslt/namespaces.h
/usr/include/libxslt/numbersInternals.h
/usr/include/libxslt/pattern.h
/usr/include/libxslt/preproc.h
/usr/include/libxslt/security.h
/usr/include/libxslt/templates.h
/usr/include/libxslt/transform.h
/usr/include/libxslt/variables.h
/usr/include/libxslt/xslt.h
/usr/include/libxslt/xsltInternals.h
/usr/include/libxslt/xsltconfig.h
/usr/include/libxslt/xsltexports.h
/usr/include/libxslt/xsltlocale.h
/usr/include/libxslt/xsltutils.h
/usr/lib64/libexslt.so
/usr/lib64/libxslt.so
/usr/lib64/pkgconfig/libexslt.pc
/usr/lib64/pkgconfig/libxslt.pc
/usr/share/aclocal/*.m4

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/libxslt/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexslt.so.0
/usr/lib64/libexslt.so.0.8.18
/usr/lib64/libxslt.so.1
/usr/lib64/libxslt.so.1.1.30

%files python
%defattr(-,root,root,-)
/usr/lib64/python*/*
