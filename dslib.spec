Summary:	Free Python library for accessing Datove schranky
Name:		dslib
Version:	2.1.0
Release:	5
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

%changelog
* Thu Jul 19 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.1.0-1
+ Revision: 810195
- version update 2.1.0

* Tue Aug 09 2011 Tomas Kindl <supp@mandriva.org> 1.6-1
+ Revision: 693765
- update to 1.6

* Sun May 29 2011 Tomas Kindl <supp@mandriva.org> 1.5.1-1
+ Revision: 681702
-update to 1.5.1

* Thu May 05 2011 Tomas Kindl <supp@mandriva.org> 1.5-1
+ Revision: 669307
- update to 1.5

* Thu Apr 21 2011 Tomas Kindl <supp@mandriva.org> 1.4.1-2
+ Revision: 656541
-fix release!
- fix python macros, license, group
- import dslib
