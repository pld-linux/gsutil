Summary:	A utility to save, restore and reboot Grandstream Budgetone phones
Summary(pl.UTF-8):	Narzędzie do zapisywania, odtwarzania i restartowania telefonów Grandstream Budgetone
Name:		gsutil
Version:	2.1
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.pkts.ca/%{name}-%{version}.tar.gz
# Source0-md5:	28010ee2e2881dd6597e27659174ee6a
URL:		http://www.pkts.ca/gsutil.shtml
Requires:	perl-base
Requires:	perl-libwww
Provides:	gsutil
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A utility to dump and restore the configuration of the Grandstream
Budgetone VOIP telephone, up to and including version 1.0.6.7 of the
firmware.

%description -l pl.UTF-8
Narzędzie do zrzucania i odtwarzania konfiguracji telefonów VOIP
Grandstream Budgetone do wersji firmware'u 1.0.6.7 włącznie.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install gsutil $RPM_BUILD_ROOT%{_bindir}/gsutil

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changelog
%attr(755,root,root) %{_bindir}/gsutil
