Summary:	Minimal FreeDOS
Summary(pl):	Minimalna wersja FreeDOSa
Name:		dosemu-freedos-minimal
Version:	2.0.26a16
Release:	1
License:	GPL
Group:		Applications/Emulators
Source0:	http://freedos.sourceforge.net/freecom/packages/binary.zip
Source1:	http://prdownloads.sourceforge.net/freedos/ke2026a16.zip
Source2:	autoexec2.bat
Source3:	config2.sys
Source4:	keybpl.exe
Source5:	egapl.exe
Source6:	shsucdx.exe
URL:		http://www.freedos.org/
BuildRequires:	unzip
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Provides:	dos
Requires:	dosemu

%description
This package contains minimal dos for use with dosemu:
FreeDOS kernel and configuration files.

%description -l pl
W pakiecie znajduje siê mimalna wersja DOSa potrzebna do uruchomienia
dosemu. Pakiet zawiera kernel FreeDOSa, autoexec.bat, config.sys
i kilka przydatnych programów.

%prep
%setup -c %{name} -q

rm -rf freedos
mkdir freedos
unzip -q -L -o %{SOURCE1} -d freedos

%build

%define _dosemudir	/var/lib/dosemu

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_dosemudir}/bootdir/freedos/doc/fdkernel
install command.com $RPM_BUILD_ROOT%{_dosemudir}/bootdir/command2.com
install kssf.com $RPM_BUILD_ROOT%{_dosemudir}/bootdir/kssf.com
install vspawn.com $RPM_BUILD_ROOT%{_dosemudir}/bootdir/vspawn.com
install %{SOURCE2} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/autoexec.bat
install %{SOURCE3} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/config.sys
install %{SOURCE4} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/keybpl.exe
install %{SOURCE5} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/egapl.exe
install %{SOURCE6} $RPM_BUILD_ROOT%{_dosemudir}/bootdir/shsucdx.exe
install freedos/bin/kernel.sys $RPM_BUILD_ROOT%{_dosemudir}/bootdir
install freedos/doc/fdkernel/* $RPM_BUILD_ROOT%{_dosemudir}/bootdir/freedos/doc/fdkernel
ln -sf dosemu/comcom.com $RPM_BUILD_ROOT%{_dosemudir}/bootdir/command.com

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_dosemudir}/bootdir/freedos
%{_dosemudir}/bootdir/kernel.sys
%config(noreplace) %verify(not size mtime md5) %{_dosemudir}/bootdir/autoexec.bat
%config(noreplace) %verify(not size mtime md5) %{_dosemudir}/bootdir/config.sys
%{_dosemudir}/bootdir/*.exe
%{_dosemudir}/bootdir/*.com
%{_dosemudir}/bootdir/freedos/*
