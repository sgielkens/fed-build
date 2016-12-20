Name:           cereal
Version:        1.1.2
Release:        1%{?dist}
Summary:        A C++ library for serialization

License:        BSD
URL:            http://uscilab.github.io/cereal/
Source0:        https://github.com/USCiLab/%{name}/archive/v%{version}.tar.gz

#BuildRequires:
#Requires:     

%description

%prep
%setup -q 

%build
# No build, library is header only
%define debug_package %{nil}
#make %{?_smp_mflags}

%install
# make_install
mkdir -p %{buildroot}/%{_includedir}
cp -rp include/cereal %{buildroot}/%{_includedir}

%files
#%doc doc/manual.pdf
%{_includedir}/cereal

%changelog
