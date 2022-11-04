Name:           python-mypy
Version:        0.982
Release:        %mkrel 1
Summary:        A static type checker for Python
Group:          Development/Python
License:        MIT and ASL 2.0
URL:            https://github.com/python/mypy
Source:         https://files.pythonhosted.org/packages/source/m/mypy/mypy-%{version}.tar.gz
Patch0:         0001-Drop-typed_ast-reqs.patch
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
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
%py_build

%install
%py_install
rm -vrf %{buildroot}%{python3_sitelib}/mypy/{test,typeshed/tests}


%files
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
