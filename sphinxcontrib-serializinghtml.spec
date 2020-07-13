#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-serializinghtml
Version  : 1.1.4
Release  : 13
URL      : https://files.pythonhosted.org/packages/ac/86/021876a9dd4eac9dae0b1d454d848acbd56d5574d350d0f835043b5ac2cd/sphinxcontrib-serializinghtml-1.1.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/ac/86/021876a9dd4eac9dae0b1d454d848acbd56d5574d350d0f835043b5ac2cd/sphinxcontrib-serializinghtml-1.1.4.tar.gz
Source1  : https://files.pythonhosted.org/packages/ac/86/021876a9dd4eac9dae0b1d454d848acbd56d5574d350d0f835043b5ac2cd/sphinxcontrib-serializinghtml-1.1.4.tar.gz.asc
Summary  : sphinxcontrib-serializinghtml is a sphinx extension which outputs "serialized" HTML files (json and pickle).
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-serializinghtml-license = %{version}-%{release}
Requires: sphinxcontrib-serializinghtml-python = %{version}-%{release}
Requires: sphinxcontrib-serializinghtml-python3 = %{version}-%{release}
Requires: flake8
Requires: mypy
BuildRequires : buildreq-distutils3
BuildRequires : flake8
BuildRequires : mypy
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs
        "serialized" HTML files (json and pickle).

%package license
Summary: license components for the sphinxcontrib-serializinghtml package.
Group: Default

%description license
license components for the sphinxcontrib-serializinghtml package.


%package python
Summary: python components for the sphinxcontrib-serializinghtml package.
Group: Default
Requires: sphinxcontrib-serializinghtml-python3 = %{version}-%{release}

%description python
python components for the sphinxcontrib-serializinghtml package.


%package python3
Summary: python3 components for the sphinxcontrib-serializinghtml package.
Group: Default
Requires: python3-core
Provides: pypi(sphinxcontrib_serializinghtml)

%description python3
python3 components for the sphinxcontrib-serializinghtml package.


%prep
%setup -q -n sphinxcontrib-serializinghtml-1.1.4
cd %{_builddir}/sphinxcontrib-serializinghtml-1.1.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583453169
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sphinxcontrib-serializinghtml
cp %{_builddir}/sphinxcontrib-serializinghtml-1.1.4/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-serializinghtml/5846f689e338684fe93c22b0c477944d5a0803f9
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sphinxcontrib-serializinghtml/5846f689e338684fe93c22b0c477944d5a0803f9

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
