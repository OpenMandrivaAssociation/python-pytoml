%define srcname pytoml

Name:		python-%{srcname}
Version:	0.1.21
Release:	2
Summary:	A TOML-0.4.0 parser/writer for Python
Group:		Development/Python
License:	BSD
URL:		https://github.com/avakar/pytoml
Source0:	https://github.com/avakar/pytoml/archive/%{srcname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python-pkg-resources

%description
This project aims at being a specs-conforming and strict parser and writer for
TOML files.

The library currently supports version 0.4.0 of the specs.

%files
%license LICENSE
%doc README.md
%{py_puresitedir}/%{srcname}
%{py_puresitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{srcname}-%{version}

%build
%py_build

%install
%py_install

%check
%__python setup.py test

