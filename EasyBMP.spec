Summary:	EasyBMP library
Summary(pl):	Biblioteka EasyBMP
Name:		EasyBMP
Version:	0.66
Release:	1
License:	LGPL
Group:		Libraries
%define		dver 0.66
Source0:	http://dl.sourceforge.net/easybmp/%{name}_%{version}.zip
# Source0-md5:	fb1b43ca5158c6eb7ad428459f0687fd
Source1:	http://dl.sourceforge.net/easybmp/%{name}_Documentation_%{dver}.zip
# Source1-md5:	7325efa8ac22826b1a3c0dd0633cb03e
URL:		http://easybmp.sourceforge.net/
BuildRequires:	unzip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Easy to use library for BMP file format handling.

%description -l pl
£atwa w u¿yciu biblioteka do obs³ugi formatu BMP.

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
