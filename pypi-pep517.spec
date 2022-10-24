#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pep517
Version  : 0.13.0
Release  : 32
URL      : https://files.pythonhosted.org/packages/4d/19/e11fcc88288f68ae48e3aa9cf5a6fd092a88e629cb723465666c44d487a0/pep517-0.13.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/4d/19/e11fcc88288f68ae48e3aa9cf5a6fd092a88e629cb723465666c44d487a0/pep517-0.13.0.tar.gz
Summary  : Wrappers to build Python packages using PEP 517 hooks
Group    : Development/Tools
License  : MIT
Requires: pypi-pep517-license = %{version}-%{release}
Requires: pypi-pep517-python = %{version}-%{release}
Requires: pypi-pep517-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
API to call PEP 517 hooks
=========================
`PEP 517 <https://www.python.org/dev/peps/pep-0517/>`_ specifies a standard
API for systems which build Python packages.

%package license
Summary: license components for the pypi-pep517 package.
Group: Default

%description license
license components for the pypi-pep517 package.


%package python
Summary: python components for the pypi-pep517 package.
Group: Default
Requires: pypi-pep517-python3 = %{version}-%{release}

%description python
python components for the pypi-pep517 package.


%package python3
Summary: python3 components for the pypi-pep517 package.
Group: Default
Requires: python3-core
Provides: pypi(pep517)
Requires: pypi(tomli)

%description python3
python3 components for the pypi-pep517 package.


%prep
%setup -q -n pep517-0.13.0
cd %{_builddir}/pep517-0.13.0
pushd ..
cp -a pep517-0.13.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1659368152
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pep517
cp %{_builddir}/pep517-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pep517-%{version}/tests/samples/pkg1/pkg1-0.5.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pep517-%{version}/tests/samples/pkg2/pkg2-0.5.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
cp %{_builddir}/pep517-%{version}/tests/samples/pkg3/pkg3-0.5.dist-info/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pep517/b2f7e71b77f14f21cd693e1c6fbe7236a8deac5f

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
