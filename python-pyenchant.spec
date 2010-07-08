%define		pname pyenchant
Summary:	Spellchecking library for Python
Summary(pl.UTF-8):	Biblioteka Pythona sprawdzająca pisownię
Name:		python-%{pname}
Version:	1.5.1
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://dl.sourceforge.net/pyenchant/%{pname}-%{version}.tar.gz
# Source0-md5:	1195bb1dae4fa0efc76f1668a35fe458
Patch0:		%{name}-ez_setup.patch
URL:		http://pyenchant.sourceforge.net/
BuildRequires:	enchant-devel >= 1.3.0
BuildRequires:	python-devel
BuildRequires:	python-setuptools >= 0.6-0.c3
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-libs
Requires:	enchant >= 1.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyEnchant is a set of language bindings and some wrapper classes to
make the excellent Enchant spellchecker available as a Python module.

%description -l pl.UTF-8
PyEnchant to zbiór dowiązań języka i klas obudowujących
udostępniających świetną bibliotekę sprawdzania pisowni Enchant jako
moduł Pythona.

%prep
%setup -q -n %{pname}-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--optimize=2 \
	--root $RPM_BUILD_ROOT \
	--single-version-externally-managed

find $RPM_BUILD_ROOT%{python_sitelib}/enchant -name '*.py' -exec rm -f {} \;
rm -rf $RPM_BUILD_ROOT%{python_sitelib}/%{pname}-%{version}-*.egg-info

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%dir %{python_sitelib}/enchant
%dir %{python_sitelib}/enchant/checker
%dir %{python_sitelib}/enchant/tokenize
%{python_sitelib}/enchant/*.py[oc]
%{python_sitelib}/enchant/checker/*.py[oc]
%{python_sitelib}/enchant/tokenize/*.py[oc]
