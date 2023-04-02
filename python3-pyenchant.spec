Summary:	Spellchecking library for Python 3
Summary(pl.UTF-8):	Biblioteka Pythona 3 sprawdzająca pisownię
Name:		python3-pyenchant
Version:	3.2.2
Release:	1
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyenchant/
Source0:	https://files.pythonhosted.org/packages/source/p/pyenchant/pyenchant-%{version}.tar.gz
# Source0-md5:	15d45b7517c80cfa5d9fa636a88e0bf9
URL:		https://pypi.org/project/pyenchant/
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools >= 1:7
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
# or enchant2 (up to 2.2?)
Requires:	enchant >= 1.6.0
Requires:	python3-libs >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyEnchant is a set of language bindings and some wrapper classes to
make the excellent Enchant spellchecker available as a Python module.

%description -l pl.UTF-8
PyEnchant to zbiór dowiązań języka i klas obudowujących
udostępniających świetną bibliotekę sprawdzania pisowni Enchant jako
moduł Pythona.

%prep
%setup -q -n pyenchant-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog README.rst
%{py3_sitescriptdir}/enchant
%{py3_sitescriptdir}/pyenchant-%{version}-py*.egg-info
