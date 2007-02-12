Summary:	APE - Advanced Petri nets Environment
Summary(pl.UTF-8):	APE - Zaawansowane środowisko sieci Petriego
Name:		ape
Version:	0.5.2.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Science
Source0:	http://fm.ia.agh.edu.pl/download/%{name}-%{version}.tar.gz
# Source0-md5:	f2649352d48bfacdaa01cb872a5ee8a3
Source1:	%{name}.desktop
URL:		http://fm.ia.agh.edu.pl/
BuildRequires:	qt-devel >= 3
BuildRequires:	qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
APE tool is intended to be an advanced environment for modelling and
analysis of Petri nets. The tool supports a few classes of low level
Petri nets: place-transition nets, priority nets, simple time nets
and simple time nets with priorities.

%description -l pl.UTF-8
APE jest narzędziem mającym dostarczać zaawansowane środowisko do
modelowania i analizy sieci Petriego. Wspiera kilka klas
niskopoziomowych sieci Petriego: sieci miejsc i przejść, sieci
priorytetowe, proste sieci czasowe oraz proste priorytetowe sieci
czasowe.

%prep
%setup -q

%build
export QTDIR=%{_prefix}
qmake
%{__make} \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/apps/%{name},%{_pixmapsdir},%{_desktopdir}}

# project is not ready yet for this
#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{name} $RPM_BUILD_ROOT%{_bindir}
install images/ape.png $RPM_BUILD_ROOT%{_pixmapsdir}
install aperc $RPM_BUILD_ROOT%{_datadir}/apps/%{name}
cp -af examples $RPM_BUILD_ROOT%{_datadir}/apps/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%{_datadir}/apps/%{name}
