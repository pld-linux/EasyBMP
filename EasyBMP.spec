Summary:	EasyBMP library
Summary(pl):	Biblioteka EasyBMP
Name:		EasyBMP
Version:	0.71
Release:	1
License:	BSD
Group:		Libraries
%define		dver 0.70.00
Source0:	http://dl.sourceforge.net/easybmp/%{name}_%{version}.zip
# Source0-md5:	84162470b5c0d4ac6a1a0ba0afa6e321
Source1:	http://dl.sourceforge.net/easybmp/%{name}_Documentation_%{dver}.zip
# Source1-md5:	c9959b86b58dd776ba068e926c5a0213
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
