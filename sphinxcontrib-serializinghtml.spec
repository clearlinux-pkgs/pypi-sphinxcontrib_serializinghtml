#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : sphinxcontrib-serializinghtml
Version  : 1.1.3
Release  : 10
URL      : https://files.pythonhosted.org/packages/cd/cc/fd7d17cfae18e5a92564bb899bc05e13260d7a633f3cffdaad4e5f3ce46a/sphinxcontrib-serializinghtml-1.1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/cd/cc/fd7d17cfae18e5a92564bb899bc05e13260d7a633f3cffdaad4e5f3ce46a/sphinxcontrib-serializinghtml-1.1.3.tar.gz
Source1  : https://files.pythonhosted.org/packages/cd/cc/fd7d17cfae18e5a92564bb899bc05e13260d7a633f3cffdaad4e5f3ce46a/sphinxcontrib-serializinghtml-1.1.3.tar.gz.asc
Summary  : No summary provided
Group    : Development/Tools
License  : BSD-2-Clause
Requires: sphinxcontrib-serializinghtml-license = %{version}-%{release}
Requires: sphinxcontrib-serializinghtml-python = %{version}-%{release}
Requires: sphinxcontrib-serializinghtml-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
sphinxcontrib-serializinghtml is a sphinx extension which outputs
"serialized" HTML files (json and pickle).

Home-page: http://sphinx-doc.org/
Author: Georg Brandl
Author-email: georg@python.org
License: BSD
Download-URL: https://pypi.org/project/sphinxcontrib-serializinghtml/
Description: 
        sphinxcontrib-serializinghtml is a sphinx extension which outputs
        "serialized" HTML files (json and pickle).
        
Platform: any
Classifier: Development Status :: 5 - Production/Stable
Classifier: Environment :: Console
Classifier: Environment :: Web Environment
Classifier: Intended Audience :: Developers
Classifier: Intended Audience :: Education
Classifier: License :: OSI Approved :: BSD License
Classifier: Operating System :: OS Independent
Classifier: Programming Language :: Python
Classifier: Programming Language :: Python :: 3
Classifier: Programming Language :: Python :: 3.5
Classifier: Programming Language :: Python :: 3.6
Classifier: Programming Language :: Python :: 3.7
Classifier: Framework :: Sphinx
Classifier: Framework :: Sphinx :: Extension
Classifier: Topic :: Documentation
Classifier: Topic :: Documentation :: Sphinx
Classifier: Topic :: Text Processing
Classifier: Topic :: Utilities
Requires-Python: >=3.5
Provides-Extra: test

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
Provides: pypi(sphinxcontrib-serializinghtml)

%description python3
python3 components for the sphinxcontrib-serializinghtml package.


%prep
%setup -q -n sphinxcontrib-serializinghtml-1.1.3
cd %{_builddir}/sphinxcontrib-serializinghtml-1.1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582918891
# -Werror is for werrorists
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
cp %{_builddir}/sphinxcontrib-serializinghtml-1.1.3/LICENSE %{buildroot}/usr/share/package-licenses/sphinxcontrib-serializinghtml/5846f689e338684fe93c22b0c477944d5a0803f9
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
