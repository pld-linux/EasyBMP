Summary:	EasyBMP library
Summary(pl):	Biblioteka EasyBMP
Name:		EasyBMP
Version:	0.65
Release:	1
License:	LGPL
Group:		Libraries
%define		dver 0.64
Source0:	http://dl.sourceforge.net/easybmp/%{name}_%{version}.zip
# Source0-md5:	0d57f6c35969354168f81fedbb4516f0
Source1:	http://dl.sourceforge.net/easybmp/%{name}_Documentation_%{dver}.zip
# Source1-md5:	d785153fc9663b964455fcb7fa126b3a
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
