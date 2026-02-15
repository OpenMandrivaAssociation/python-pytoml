%define module pytoml
%bcond tests 1

Name:		python-%{module}
Version:	0.1.21
Release:	5
Summary:	A TOML-0.4.0 parser/writer for Python
Group:		Development/Python
License:	BSD
URL:		https://github.com/avakar/pytoml
Source0:	https://github.com/avakar/pytoml/archive/%{module}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
This project aims at being a specs-conforming and strict parser and writer for
TOML files.

The library currently supports version 0.4.0 of the specs.

%prep -a
# Remove bundled egg-info
rm -rf %{module}.egg-info

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -v test/
%endif

%files
%license LICENSE
%doc README.md
%{py_puresitedir}/%{module}
%{py_puresitedir}/%{module}-%{version}-py%{py_ver}.egg-info
