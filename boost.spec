# This is a spec file for boost
# rpmbuild -v -bb --clean SPECS/boost.spec

%define _topdir     /usr/src/rpm
%define name        boost
%define release     1
%define version     67_0
%define buildroot %{_topdir}/%{name}_%{release}_%{version}-root

BuildRoot:  %{buildroot}
Summary:        Boost provides free portable peer-reviewed C++ libraries.
License:        GPL
Name:           %{name}
Version:        %{version}
Release:        %{release}
Source:         %{name}_%{release}_%{version}.tar.bz2
Prefix:         /usr
Group:          Development/Tools

%description
Boost provides free portable peer-reviewed C++ libraries. The emphasis is on portable libraries which work well with the C++ Standard Library. 

%prep
%setup -q -n %{name}_%{release}_%{version}

%build
./bootstrap.sh

%install
./b2 -d1 -j2 --with-thread --with-filesystem --with-python --with-regex -sHAVE_ICU=1 --with-program_options --with-system link=shared release toolset=gcc stage --prefix=$RPM_BUILD_ROOT/usr
./b2 -d1 -j2 --with-thread --with-filesystem --with-python --with-regex -sHAVE_ICU=1 --with-program_options --with-system link=shared release toolset=gcc install --prefix=$RPM_BUILD_ROOT/usr

%files
%defattr(-,root,root)
/usr/include/boost
/usr/lib/libboost_filesystem.so
/usr/lib/libboost_filesystem.so.1.67.0
/usr/lib/libboost_program_options.so
/usr/lib/libboost_program_options.so.1.67.0
/usr/lib/libboost_python27.so
/usr/lib/libboost_python27.so.1.67.0
/usr/lib/libboost_regex.so
/usr/lib/libboost_regex.so.1.67.0
/usr/lib/libboost_system.so
/usr/lib/libboost_system.so.1.67.0
/usr/lib/libboost_thread.so
/usr/lib/libboost_thread.so.1.67.0