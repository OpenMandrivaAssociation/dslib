Summary:	Free Python library for accessing Datove schranky
Name:		dslib
Version:	2.1.0
Release:	6
Source0:	http://www.nic.cz/public_media/datove_schranky/releases/datovka-2.1.1/src/%{name}-%{version}.tar.gz
# Upstream stopped at Python 2. This port keeps the 2.1.0 API on Python 3.15.
Patch0:		dslib-2.1.0-python315.patch
License:	LGPL
Group:		System/Libraries
URL:		https://labs.nic.cz/datove-schranky/
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(pyopenssl)
Requires:	python%{pyver}dist(pyasn1)
Requires:	python%{pyver}dist(sudsds)

%description
dslib is a Python library for accessing a 'Databox' - an
electronic communication interface endorsed by the Czech government.

%files
%{py_puresitedir}/dslib
%{py_puresitedir}/dslib-%{version}-py%{pyver}.egg-info
%{_datadir}/dslib
