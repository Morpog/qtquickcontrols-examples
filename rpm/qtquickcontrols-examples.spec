Name:       qt5-qtquickcontrols-examples
Summary:    Qt Quick Controls Examples
Version:    5.1.0
Release:    mer1
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source0:    qtquickcontrols-examples-5.1.0.tar.xz
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtdeclarative-qtquick-devel
BuildRequires:  qt5-qtv8-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-qtquickcontrols
BuildRequires:  fdupes

%description
This package contains the Qt Quick Controls Examples



#### Build section

%prep
%setup -q -n qtquickcontrols-examples-5.1.0

%build
export QTDIR=/usr/share/qt5
touch .git # To make sure syncqt is used

%qmake5
make %{?_smp_flags}

%install
rm -rf %{buildroot}
%qmake5_install
# Fix wrong path in pkgconfig files
#find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
#-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
#find %{buildroot}%{_libdir} -type f -name '*.prl' \
#-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;
# Remove unneeded .la files
#rm -f %{buildroot}/%{_libdir}/*.la
#%fdupes %{buildroot}/%{_includedir}


#### Pre/Post section

%post
/sbin/ldconfig
%postun
/sbin/ldconfig

#### File section

%files
%defattr(-,root,root,-)
%{_libdir}/qt5/examples/*

