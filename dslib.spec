%define name dslib
%define version 1.4.1
%define unmangled_version 1.4.1
%define release 1
%include %{_rpmconfigdir}/macros.python

Summary:	dslib is a free Python library for accessing Datove schranky
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{unmangled_version}.tar.gz
License:	GNU LGPL
Group:		Development/Libraries
BuildArch:	noarch
Requires:	python-OpenSSL
BuildRequires:	python-setuptools
URL:		http://labs.nic.cz/datove-schranky/

%description
dslib is a Python library for accessing a 'Databox' - an 
electronic communication interface endorsed by the Czech government.

%prep
%setup -n %{name}-%{unmangled_version} -n %{name}-%{unmangled_version} -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed \
	--root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%dir %{py_sitedir}/%{name}*
%{py_sitedir}/%{name}*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

