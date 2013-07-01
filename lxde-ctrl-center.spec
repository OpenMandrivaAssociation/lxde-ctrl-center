Summary:	LXDE Control Center
Name:		lxde-ctrl-center
Version:	0.1.0
Release:	1
Group:		System/Configuration/Other
License:	GPLv3+
Url:		http://code.google.com/p/lxde-ctrl-center/
Source0:	http://code.google.com/p/lxde-ctrl-center/files/%{name}-%{version}.tar.gz
Source1:	clouds.png
Source2:	bg.png
BuildRequires:	gettext
BuildRequires:	python
Requires:	pygtk2.0
Requires:	python-webkitgtk
Requires:	python-simplejson
Requires:	beesu
Requires:	lxde-common
BuildArch:	noarch

#drakuser
Suggests:	userdrake
#drakauth, drakkeyboard, /usr/sbin/drakscanner, /usr/sbin/diskdrake, /usr/sbin/draksound, drakups, /usr/sbin/drakxservices, draklocale, drakboot, draklog, /usr/sbin/drakedm
Suggests:	drakxtools-curses
#/usr/sbin/drakguard
Suggests:	drakguard
#obconf
Suggests:	obconf
#lxappearance
Suggests:	lxappearance
#pcmanfm --desktop-pref
Suggests:	pcmanfm
#lxrandr
Suggests:	lxrandr
#xscreensaver-demo
Suggests:	xscreensaver
#drakfont, drakclock, /usr/sbin/draksec
Suggests:	drakxtools
#/usr/sbin/harddrake2
Suggests:	harddrake-ui
#XFdrake, /usr/sbin/mousedrake
Suggests:	drakx-kbd-mouse-x11
#system-config-printer
Suggests:	system-config-printer
#mdvinput
Suggests:	mdvinput
#pavucontrol
Suggests:	pavucontrol
#drakproxy, /usr/sbin/drakfirewall, drakgw
Suggests:	drakx-net-text
#vpnpptp
Suggests:	vpnpptp-allde
#system-config-nfs
Suggests:	system-config-nfs
#system-config-samba
Suggests:	system-config-samba
#gigolo
Suggests:	gigolo
#drakhosts
Suggests:	drakx-net
#drakrpm, drakrpm-edit-media, drakrpm-update
Suggests:	rpmdrake
#libfm-pref-apps
Suggests:	libfm
#fskbsetting
Suggests:	fskbsetting
#/usr/sbin/msecgui
Suggests:	msec-gui
#nm-connection-editor
Suggests:	networkmanager-applet
#add2sudoers, rmfromsudoers
Suggests:	xsudo-sudoers

%description
LXDE Control Center is united launch tools for DrakX
and LXDE configuration programs.

%prep
%setup -q -n %{name}
cp -f %{SOURCE1} ./share/%{name}/frontend/images/
cp -f %{SOURCE2} ./share/%{name}/frontend/images/
sed -i -e 's/"beesu drakconnect"/"nm-connection-editor"/g' ./share/%{name}/items/x0002x
sed -i -e '/"beesu drakgw"/d' ./share/%{name}/items/x0002x

%build
./make build_pkg

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}

cp -rf ./bin/* %{buildroot}%{_bindir}/
cp -rf ./share/* %{buildroot}%{_datadir}/

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}

