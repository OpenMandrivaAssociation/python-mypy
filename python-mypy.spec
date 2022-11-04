Name:           python-mypy
Version:        0.982
Release:        %mkrel 1
Summary:        A static type checker for Python
Group:          Development/Python

# The files under lib-python and lib-typing/3.2 are Python-licensed, but this
# package does not include those files
# mypy/typeshed is ASL 2.0
License:        MIT and ASL 2.0
URL:            https://github.com/python/mypy
Source:         %{pypi_source mypy}
Patch0:         0001-Drop-typed_ast-reqs.patch
BuildArch:      noarch

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%package -n python3-mypy
Summary:        A static type checker for Python
Group:          Development/Python
%{?python_provide:%python_provide python3-mypy}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

# Needed to generate the man pages
BuildRequires:  help2man
BuildRequires:  python3dist(mypy-extensions) >= 0.4.0
BuildRequires:  python3dist(mypy-extensions) < 0.5.0

%description -n python3-mypy
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%prep
%autosetup -n mypy-%{version} -p1

# drop bundled egg-info
rm -rf *.egg-info/

%build
%py3_build

%install
%py3_install
rm -vrf %{buildroot}%{python3_sitelib}/mypy/{test,typeshed/tests}

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/mypy.1 \
        %{buildroot}%{_bindir}/mypy

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy stubgen %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/stubgen.1 \
        %{buildroot}%{_bindir}/stubgen

%files -n python3-mypy
%license LICENSE
%doc README.md
%{python3_sitelib}/mypy
%{python3_sitelib}/mypyc
%{python3_sitelib}/mypy-*.egg-info
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/dmypy
%{_bindir}/stubgen
%{_bindir}/stubtest
%{_mandir}/man1/mypy.1*
%{_mandir}/man1/stubgen.1*
