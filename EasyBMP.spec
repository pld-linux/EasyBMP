Summary:	EasyBMP library
Summary(pl.UTF-8):   Biblioteka EasyBMP
Name:		EasyBMP
Version:	1.06
Release:	1
License:	BSD
Group:		Libraries
%define		dver 1.00.00
Source0:	http://dl.sourceforge.net/easybmp/%{name}_%{version}.zip
# Source0-md5:	c2d547a6574fd31a62df5e82783d342d
Source1:	http://dl.sourceforge.net/easybmp/%{name}_Documentation_%{dver}.zip
# Source1-md5:	9b9f50c20b07bdeb5f38fd23326cf31c
URL:		http://easybmp.sourceforge.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use library for BMP file format handling.

%description -l pl.UTF-8
Łatwa w użyciu biblioteka do obsługi formatu BMP.

%prep
%setup -q -c -a 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/EasyBMP

install *.h $RPM_BUILD_ROOT%{_includedir}/EasyBMP

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc EasyBMP_ChangeLog.txt EasyBMP_UserManual.pdf
%{_includedir}/%{name}
