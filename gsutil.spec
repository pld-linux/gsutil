Summary:	A utility to save, restore and reboot Grandstream Budgetone phones
Name:		gsutil
Version:	2.1
Release:	1
Group:		Applications/System
Source0:	http://www.pkts.ca/%{name}-%{version}.tar.gz
# Source0-md5:	28010ee2e2881dd6597e27659174ee6a
License:	GPL
URL:		http://www.pkts.ca/gsutil.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch
Requires:	perl
Requires:	perl-libwww
Provides:	gsutil

%description
A utility to dump and restore the configuration of the Grandstream
Budgetone VOIP telephone, up to and including version 1.0.6.7 of the
firmware.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp %{_builddir}/%{name}-%{version}/gsutil $RPM_BUILD_ROOT%{_bindir}/gsutil

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gsutil
%doc README Changelog
