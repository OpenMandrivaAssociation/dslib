%define name dslib
%define version 1.4.1
%define unmangled_version 1.4.1
%define release %mkrel 2

Summary:	dslib is a free Python library for accessing Datove schranky
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{unmangled_version}.tar.gz
License:	LGPL
Group:		System/Libraries
BuildArch:	noarch
Requires:	python-OpenSSL
BuildRequires:	python-setuptools
URL:		http://labs.nic.cz/datove-schranky/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%dir %{py_puresitedir}/%{name}*
%{py_puresitedir}/%{name}*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*

