%define srcname pytoml

Name:           python-%{srcname}
Version:	0.1.20
Release:        4
Summary:        A TOML-0.4.0 parser/writer for Python
Group:		Development/Python
License:        BSD
URL:            https://github.com/avakar/pytoml
Source0:        https://github.com/avakar/pytoml/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python2)
BuildRequires:  pythonegg(setuptools)
BuildRequires:  python2-pkg-resources
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3egg(setuptools)
BuildRequires:  python-pkg-resources

%description
This project aims at being a specs-conforming and strict parser and writer for
TOML files.

The library currently supports version 0.4.0 of the specs.

%package -n python2-%{srcname}
Summary:        A TOML-0.4.0 parser/writer for Python
Group:		Development/Python

%description -n python2-%{srcname}
This project aims at being a specs-conforming and strict parser and writer for
TOML files.

The library currently supports version 0.4.0 of the specs.

%prep
%setup -q -n %{srcname}-%{version}
cp -a . %{py2dir}


%build
%__python setup.py build

pushd %{py2dir}
%{__python2} setup.py build
popd

%install
pushd %{py2dir}
%{__python2} setup.py install --skip-build --root %{buildroot}
popd

%__python setup.py install --skip-build --root %{buildroot}

%check
%__python setup.py test

pushd %{py2dir}
%__python2 setup.py test
popd


%files
%{py_puresitedir}/%{srcname}
%{py_puresitedir}/%{srcname}-%{version}-py%{py_ver}.egg-info

%files -n python2-%{srcname}
%{py2_puresitedir}/%{srcname}
%{py2_puresitedir}/%{srcname}-%{version}-py%{py2_ver}.egg-info
