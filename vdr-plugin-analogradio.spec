%define plugin	analogradio

Summary:	VDR plugin: Source device for analog radio tuner devices
Name:		vdr-plugin-%plugin
Version:	0.1.3a
Release:	21
Group:		Video
License:	GPL
URL:		http://tankwar.de/analogradio.php
Source:		http://tankwar.de/files/analogradio/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin enables VDR to get input from an analog radio device, as it can be
found on many analog tv tuner cards. It uses video4linux functions to control
/dev/radioX.

%prep
%setup -q -n %plugin-%version
%vdr_plugin_prep

%vdr_plugin_params_begin %plugin
# execute command after muting the radio device
var=AFTER_MUTE
param=--after=AFTER_MUTE
# execute command before unmuting the radio device
var=BEFORE_UNMUTE
param=--before=BEFORE_UNMUTE
# Audio mode:
# OSS (default)
# RAW
# ALSA (not supported)
var=MODE
param=--mode=MODE
# radio device (default /dev/radio)
var=RADIO_DEVICE
param=--devradio=RADIO_DEVICE
# audio device (default /dev/dsp)
var=AUDIO_DEVICE
param=--devaudio=AUDIO_DEVICE
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
%vdr_plugin_install

install -D -m755 tools/adr2vdr.sh %buildroot%_bindir/adr2vdr.sh

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/adr2vdr.sh




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3a-19mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.3a-18mdv2009.1
+ Revision: 359276
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3a-17mdv2009.0
+ Revision: 197893
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3a-16mdv2009.0
+ Revision: 197625
- add vdr_plugin_prep
- bump buildrequires on vdr-devel

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3a-15mdv2008.1
+ Revision: 145010
- rebuild for new vdr

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.3a-14mdv2008.1
+ Revision: 144968
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3a-13mdv2008.1
+ Revision: 103054
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3a-12mdv2008.0
+ Revision: 49963
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3a-11mdv2008.0
+ Revision: 42050
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.3a-10mdv2008.0
+ Revision: 22690
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-9mdv2007.0
+ Revision: 90885
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-8mdv2007.1
+ Revision: 73938
- rebuild for new vdr
- Import vdr-plugin-analogradio

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-7mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-6mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-5mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-4mdv2007.0
- rebuild for new vdr

* Tue Jun 20 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-3mdv2007.0
- rebuild for new vdr

* Mon Jun 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-2mdv2007.0
- rebuild for new vdr

* Sun Jun 04 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3a-1mdv2007.0
- initial Mandriva release

