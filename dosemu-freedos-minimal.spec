Summary:	Minimal FreeDOS
Summary(pl):	Minimalna wersja FreeDOSa
Name:		dosemu-freedos-minimal
Version:	2.0.33_16
Release:	2
License:	GPL
Group:		Applications/Emulators
Source0:	http://dl.sourceforge.net/freedos/ke2033_16.zip
# Source0-md5:	07a702a337d6c5b1ae0709ce39e29212
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
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dosemudir	/var/lib/dosemu
# extract to lowercase
%define		__unzip		unzip -L

%description
This package contains minimal dos for use with dosemu:
FreeDOS kernel and configuration files.

%description -l pl
W pakiecie znajduje siê mimalna wersja DOS-a potrzebna do uruchomienia
dosemu. Pakiet zawiera kernel FreeDOSa, autoexec.bat, config.sys
i kilka przydatnych programów.

%prep
%setup -c %{name} -q

rm -f bin/autoxec.bat bin/config.sys

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_dosemudir}/bootdir/freedos/{bin,help,nls}

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
%doc doc/{bugs,config,contrib,history,intfns,mkboot,nls,readme,sys}.txt
%config(noreplace) %verify(not size mtime md5) %{_dosemudir}/bootdir/autoexec.bat
%config(noreplace) %verify(not size mtime md5) %{_dosemudir}/bootdir/config.sys
%{_dosemudir}/bootdir/command.com
%{_dosemudir}/bootdir/egapl.exe
%{_dosemudir}/bootdir/install.bat
%{_dosemudir}/bootdir/kernel.sys
%{_dosemudir}/bootdir/keybpl.exe
%{_dosemudir}/bootdir/shsucdx.exe
%{_dosemudir}/bootdir/sys.com
%dir %{_dosemudir}/bootdir/freedos
%dir %{_dosemudir}/bootdir/freedos/bin
%dir %{_dosemudir}/bootdir/freedos/help
%dir %{_dosemudir}/bootdir/freedos/nls
