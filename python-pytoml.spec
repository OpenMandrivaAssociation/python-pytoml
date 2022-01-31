%define srcname pytoml

Name:           python-%{srcname}
Version:	0.1.21
Release:        1
Summary:        A TOML-0.4.0 parser/writer for Python
Group:		Development/Python
License:        BSD
URL:            https://github.com/avakar/pytoml
Source0:        https://github.com/avakar/pytoml/archive/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
BuildRequires:  python-pkg-resources

%description
This project aims at being a specs-conforming and strict parser and writer for
TOML files.

The library currently supports version 0.4.0 of the specs.

%prep
%setup -q -n %{srcname}-%{version}

%build
%__python setup.py build

%install

%__python setup.py install --skip-build --root %{buildroot}

%check
%__python setup.py test


%files
%{py_puresitedir}/%{srcname}
%{py_puresitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info
