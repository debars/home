# $Id: bbkeys.spec.in,v 1.2 2005/03/05 16:59:07 vanrijn Exp $

%define name		bbkeys
%define version		0.9.1
%define release		1
%define builddir	$RPM_BUILD_DIR/%{name}-%{version}
%define x11_libdir	/usr/X11R6/lib

Summary: A completely configurable key-combo grabber for blackbox.
Name:		%{name}
Version:	%{version}
Release:	%{release}
License: GPL
Group: User Interface/Desktops
URL: http://bbkeys.sourceforge.net/
Source: http://bbkeys.sourceforge.net/downloads/%{name}-%{version}.tar.gz
BuildRequires: XFree86-devel, gcc-c++
BuildRoot: %{_tmppath}/%{name}-root

%description
bbkeys is a configurable key-grabber designed for the blackbox window manager
which is written by Brad Hughes.  Thanks to it (and blackbox) being
EWMH-compliant, it also works well with any EWMH-compliant window manager
(openbox, Gnome, KDE, etc.).  It was based on the bbtools object code
created by John Kennis, but has been completely re-written for versions
0.9.0 and greater.  Blackbox 0.70.0 (on which it is dependent) now
provides a common library, which bbkeys 0.9.0 makes use of. 
bbkeys is easily configurable via directly hand-editting the user's
~/.bbkeysrc file, or by using the GUI total blackbox configurator, bbconf.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root) 
%doc AUTHORS BUGS ChangeLog LICENSE NEWS README TODO
%exclude %{_prefix}/share/doc
%{_bindir}/*
%dir %{_datadir}/bbkeys
%config %{_datadir}/bbkeys/*
%{_mandir}/man?/*
 
%changelog 
* Sat Mar  5 2005 Jason 'vanRijn' Kasper <vR@movingparts.net>
- basing on previous work... updating for 0.9.0

* Fri Nov  7 2003 Matthias Saou <http://freshrpms.net/> - 0.8.6-3.fr
- Rebuild for Fedora Core.

* Mon Mar 31 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Rebuilt for Red Hat Linux 9.

* Thu Mar  6 2003 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Update to 0.8.6.

* Tue Aug 13 2002 Matthias Saou <matthias.saou@est.une.marmotte.net>
- Spec file cleanup.

* Sat Jan 12 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing README.bbkeys and adding BUGS and NEWS

* Sat Jan 5 2002 Jason 'vanRijn' Kasper <vR@movingparts.net>
- gzipping man pages by default and changing file list to reflect this

* Mon Nov 5 2001 Jason 'vanRijn' Kasper <vR@movingparts.net>
- removing bbkeysConfigC and replacing with bbkeysconf.pl

* Tue Sep 18 2001 Jason Kasper <vR@movingparts.net>
- changing to a dynamically-created bbkeys.spec

* Sun Aug 5 2001 Jason Kasper <vR@movingparts.net>
- added to file list for newly included files (docs and man pages)
- install to %{prefix} instead of /usr

* Sun May 6 2001 Hollis Blanchard <hollis@terraplex.com> 
- removed file list in favor of explicit %files section 
- install to /usr instead of /usr/local 
- buildroot = /var/tmp/bbkeys-buildroot instead of /tmp/buildroot

