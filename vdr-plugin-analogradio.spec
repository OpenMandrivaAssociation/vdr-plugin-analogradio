
%define plugin	analogradio
%define name	vdr-plugin-%plugin
%define version	0.1.3a
%define rel	14

Summary:	VDR plugin: Source device for analog radio tuner devices
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://tankwar.de/analogradio.php
Source:		http://tankwar.de/files/analogradio/vdr-%plugin-%version.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin enables VDR to get input from an analog radio device, as it can be
found on many analog tv tuner cards. It uses video4linux functions to control
/dev/radioX.

%prep
%setup -q -n %plugin-%version

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
rm -rf %{buildroot}
%vdr_plugin_install

install -D -m755 tools/adr2vdr.sh %buildroot%_bindir/adr2vdr.sh

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
%{_bindir}/adr2vdr.sh


