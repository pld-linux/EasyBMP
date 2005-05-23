Summary:	EasyBMP library
Summary(pl):	Biblioteka EasyBMP
Name:		EasyBMP
Version:	0.61
Release:	1
License:	LGPL
Group:		Libraries
%define		dver 0.57b
Source0:	http://dl.sourceforge.net/easybmp/%{name}_%{version}.zip
# Source0-md5:	32e42f5b407a1b208e49075d0256909f
Source1:	http://dl.sourceforge.net/easybmp/%{name}_Documentation_%{dver}.zip
# Source1-md5:	99dea20d75bd55557a1817178aab58b8
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
%doc EasyBMP_ChangeLog.txt EasyBMP_Documentation_%{dver}/EasyBMP_UserManual.pdf
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*
