#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Capture stdout, stderr easily
Summary(pl.UTF-8):	Łatwe przechwytywanie stdout, stderr
Name:		python-iocapture
Version:	0.1.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/iocapture/
Source0:	https://files.pythonhosted.org/packages/source/i/iocapture/iocapture-%{version}.tar.gz
# Source0-md5:	c32650e27e2efa89ac62b88c0a4fe0dc
URL:		https://pypi.org/project/iocapture/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Capture stdout, stderr easily.

%description -l pl.UTF-8
Łatwe przechwytywanie stdout, stderr.

%package -n python3-iocapture
Summary:	Capture stdout, stderr easily
Summary(pl.UTF-8):	Łatwe przechwytywanie stdout, stderr
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-iocapture
Capture stdout, stderr easily.

%description -n python3-iocapture -l pl.UTF-8
Łatwe przechwytywanie stdout, stderr.

%package apidocs
Summary:	API documentation for Python iocapture module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona iocapture
Group:		Documentation

%description apidocs
API documentation for Python iocapture module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona iocapture.

%prep
%setup -q -n iocapture-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst changes.rst
%{py_sitescriptdir}/iocapture
%{py_sitescriptdir}/iocapture-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-iocapture
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst changes.rst
%{py3_sitescriptdir}/iocapture
%{py3_sitescriptdir}/iocapture-%{version}-py*.egg-info
%endif
