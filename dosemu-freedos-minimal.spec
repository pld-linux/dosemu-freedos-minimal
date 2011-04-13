Summary:	Minimal FreeDOS
Summary(pl.UTF-8):	Minimalna wersja FreeDOSa
Name:		dosemu-freedos-minimal
Version:	2.0.39
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/freedos/ke2039_86f32.zip
# Source0-md5:	1e1c8abfd8db425a18fd5bce389c752a
Source2:	autoexec2.bat
Source3:	config2.sys
Source4:	keybpl.exe
# Source4-md5:	53e265897c9fc6aa983f12b59d9861b4
Source5:	egapl.exe
# Source5-md5:	226641c2370aac17d969d83e3f86a3a9
Source6:	shsucdx.exe
# Source6-md5:	ea564329c456ff4dd3a3c21c04f5a185
URL:		http://www.freedos.org/
BuildRequires:	unzip
Requires:	dosemu
Provides:	dos
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dosemudir	/var/lib/dosemu
# extract to lowercase
%define		__unzip		unzip -L

%description
This package contains minimal dos for use with dosemu: FreeDOS kernel
and configuration files.

%description -l pl.UTF-8
W pakiecie znajduje się minimalna wersja DOS-a potrzebna do
uruchomienia dosemu. Pakiet zawiera kernel FreeDOSa, autoexec.bat,
config.sys i kilka przydatnych programów.

%prep
%setup -q -c

rm -f bin/autoxec.bat bin/config.sys

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_dosemudir}/bootdir/freedos/{bin,doc,help,nls}

install bin/* $RPM_BUILD_ROOT%{_dosemudir}/bootdir
install %{SOURCE2} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/autoexec.bat
install %{SOURCE3} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/config.sys
install %{SOURCE4} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/keybpl.exe
install %{SOURCE5} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/egapl.exe
install %{SOURCE6} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/shsucdx.exe

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/{bugs,config,contrib,history,intfns,mkboot,nls,readme,sys}.txt
%config(noreplace) %verify(not md5 mtime size) %{_dosemudir}/bootdir/autoexec.bat
%config(noreplace) %verify(not md5 mtime size) %{_dosemudir}/bootdir/config.sys
%{_dosemudir}/bootdir/country.sys
%{_dosemudir}/bootdir/egapl.exe
%{_dosemudir}/bootdir/install.bat
%{_dosemudir}/bootdir/kernel.sys
%{_dosemudir}/bootdir/keybpl.exe
%{_dosemudir}/bootdir/kwc8632.map
%{_dosemudir}/bootdir/shsucdx.exe
%{_dosemudir}/bootdir/sys.com
%dir %{_dosemudir}/bootdir/freedos
%dir %{_dosemudir}/bootdir/freedos/bin
%dir %{_dosemudir}/bootdir/freedos/doc
%dir %{_dosemudir}/bootdir/freedos/help
%dir %{_dosemudir}/bootdir/freedos/nls
