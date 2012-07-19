Summary:	dslib is a free Python library for accessing Datove schranky
Name:		dslib
Version:	2.1.0
Release:	1
Source0:	http://www.nic.cz/public_media/datove_schranky/releases/datovka-2.1.1/src/%{name}-%{version}.tar.gz
License:	LGPL
Group:		System/Libraries
BuildArch:	noarch
Requires:	python-OpenSSL
BuildRequires:	python-setuptools
URL:		http://labs.nic.cz/datove-schranky/

%description
dslib is a Python library for accessing a 'Databox' - an 
electronic communication interface endorsed by the Czech government.

%prep
%setup -n %{name}-%{version} -n %{name}-%{version} -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --single-version-externally-managed \
	--root=%{buildroot}

%files
%dir %{py_puresitedir}/%{name}*
%{py_puresitedir}/%{name}*/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
