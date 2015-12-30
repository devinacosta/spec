Name:		ssdb	
Version:	1.9
Release:	1%{?dist}
Summary:	SSDB A high performance NoSQL database supporting many data structures, an alternative to Redis.

Group:		Database	
License:	GPL
URL:		http://ssdb.io
Source0:	ssdb-1.9.tar
BuildRoot:      %{_tmppath}/%{name}-%{version}
#BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires:	
#Requires:	

%description
A high performance NoSQL database supporting many data structures, an alternative to Redis.


%prep
%setup -q

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT/usr/local/ssdb

%post
chmod -R og-w $RPM_BUILD_ROOT/usr/local/ssdb/*
chmod -R o-rx $RPM_BUILD_ROOT/usr/local/ssdb/*

%clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/local/ssdb
/usr/local/ssdb/deps
/usr/local/ssdb/deps/cpy/Eval.g
/usr/local/ssdb/deps/cpy/Eval.py
/usr/local/ssdb/deps/cpy/Expr.g
/usr/local/ssdb/deps/cpy/ExprLexer.py
/usr/local/ssdb/deps/cpy/ExprParser.py
/usr/local/ssdb/deps/cpy/Makefile
/usr/local/ssdb/deps/cpy/Readme.txt
/usr/local/ssdb/deps/cpy/antlr3/__init__.py
/usr/local/ssdb/deps/cpy/antlr3/compat.py
/usr/local/ssdb/deps/cpy/antlr3/constants.py
/usr/local/ssdb/deps/cpy/antlr3/dfa.py
/usr/local/ssdb/deps/cpy/antlr3/dottreegen.py
/usr/local/ssdb/deps/cpy/antlr3/exceptions.py
/usr/local/ssdb/deps/cpy/antlr3/extras.py
/usr/local/ssdb/deps/cpy/antlr3/main.py
/usr/local/ssdb/deps/cpy/antlr3/recognizers.py
/usr/local/ssdb/deps/cpy/antlr3/streams.py
/usr/local/ssdb/deps/cpy/antlr3/tokens.py
/usr/local/ssdb/deps/cpy/antlr3/tree.py
/usr/local/ssdb/deps/cpy/antlr3/treewizard.py
/usr/local/ssdb/deps/cpy/antlr3/__init__.pyc
/usr/local/ssdb/deps/cpy/antlr3/constants.pyc
/usr/local/ssdb/deps/cpy/antlr3/dfa.pyc
/usr/local/ssdb/deps/cpy/antlr3/exceptions.pyc
/usr/local/ssdb/deps/cpy/antlr3/recognizers.pyc
/usr/local/ssdb/deps/cpy/antlr3/tokens.pyc
/usr/local/ssdb/deps/cpy/antlr3/compat.pyc
/usr/local/ssdb/deps/cpy/antlr3/streams.pyc
/usr/local/ssdb/deps/cpy/antlr3/tree.pyc
/usr/local/ssdb/deps/cpy/cpy
/usr/local/ssdb/deps/cpy/cpy.bat
/usr/local/ssdb/deps/cpy/cpy.py
/usr/local/ssdb/deps/cpy/engine.py
/usr/local/ssdb/deps/cpy/samples/class.cpy
/usr/local/ssdb/deps/cpy/samples/extends.cpy
/usr/local/ssdb/deps/cpy/samples/foreach.cpy
/usr/local/ssdb/deps/cpy/samples/function.cpy
/usr/local/ssdb/deps/cpy/samples/hello.cpy
/usr/local/ssdb/deps/cpy/samples/list.cpy
/usr/local/ssdb/deps/cpy/samples/object.cpy
/usr/local/ssdb/deps/cpy/samples/simple_client.cpy
/usr/local/ssdb/deps/cpy/samples/simple_server.cpy
/usr/local/ssdb/deps/cpy/samples/stdin.cpy
/usr/local/ssdb/deps/cpy/samples/test.cpy
/usr/local/ssdb/deps/cpy/engine.pyc
/usr/local/ssdb/deps/cpy/ExprLexer.pyc
/usr/local/ssdb/deps/cpy/ExprParser.pyc
/usr/local/ssdb/deps/cpy/Eval.pyc
/usr/local/ssdb/ssdb-server
/usr/local/ssdb/ssdb.conf
/usr/local/ssdb/ssdb_slave.conf
/usr/local/ssdb/api
/usr/local/ssdb/api/README.md
/usr/local/ssdb/api/cpp/README.md
/usr/local/ssdb/api/cpp/SSDB_client.h
/usr/local/ssdb/api/cpp/libssdb-client.a
/usr/local/ssdb/api/cpy/SSDB.cpy
/usr/local/ssdb/api/cpy/demo.cpy
/usr/local/ssdb/api/php/SSDB.php
/usr/local/ssdb/api/php/demo.php
/usr/local/ssdb/api/php/perf.php
/usr/local/ssdb/api/python/SSDB.py
/usr/local/ssdb/api/python/demo.py
/usr/local/ssdb/api/python/SSDB.pyc
/usr/local/ssdb/ssdb-bench
/usr/local/ssdb/ssdb-cli
/usr/local/ssdb/ssdb_cli
/usr/local/ssdb/ssdb_cli/cluster.cpy
/usr/local/ssdb/ssdb_cli/exporter.cpy
/usr/local/ssdb/ssdb_cli/flushdb.cpy
/usr/local/ssdb/ssdb_cli/importer.cpy
/usr/local/ssdb/ssdb_cli/util.cpy
/usr/local/ssdb/ssdb-cli.cpy
/usr/local/ssdb/ssdb-dump
/usr/local/ssdb/ssdb-repair
/usr/local/ssdb/api/python/SSDB.pyo
/usr/local/ssdb/api/python/demo.pyc
/usr/local/ssdb/api/python/demo.pyo
/usr/local/ssdb/deps/cpy/Eval.pyo
/usr/local/ssdb/deps/cpy/ExprLexer.pyo
/usr/local/ssdb/deps/cpy/ExprParser.pyo
/usr/local/ssdb/deps/cpy/antlr3/__init__.pyo
/usr/local/ssdb/deps/cpy/antlr3/compat.pyo
/usr/local/ssdb/deps/cpy/antlr3/constants.pyo
/usr/local/ssdb/deps/cpy/antlr3/dfa.pyo
/usr/local/ssdb/deps/cpy/antlr3/dottreegen.pyc
/usr/local/ssdb/deps/cpy/antlr3/dottreegen.pyo
/usr/local/ssdb/deps/cpy/antlr3/exceptions.pyo
/usr/local/ssdb/deps/cpy/antlr3/extras.pyc
/usr/local/ssdb/deps/cpy/antlr3/extras.pyo
/usr/local/ssdb/deps/cpy/antlr3/main.pyc
/usr/local/ssdb/deps/cpy/antlr3/main.pyo
/usr/local/ssdb/deps/cpy/antlr3/recognizers.pyo
/usr/local/ssdb/deps/cpy/antlr3/streams.pyo
/usr/local/ssdb/deps/cpy/antlr3/tokens.pyo
/usr/local/ssdb/deps/cpy/antlr3/tree.pyo
/usr/local/ssdb/deps/cpy/antlr3/treewizard.pyc
/usr/local/ssdb/deps/cpy/antlr3/treewizard.pyo
/usr/local/ssdb/deps/cpy/cpy.pyc
/usr/local/ssdb/deps/cpy/cpy.pyo
/usr/local/ssdb/deps/cpy/engine.pyo


%doc



%changelog

