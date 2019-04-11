Summary: Object oriented programming environment for real-time audio and video processing
Name: supercollider
Version: 3.10.2
Release: 1%{?dist}
License: GPL
Group: Applications/Multimedia
URL: https://supercollider.github.io/
Source0: https://github.com/supercollider/supercollider/releases/download/Version-%{version}/SuperCollider-%{version}-Source-linux.tar.bz2

Requires: qjackctl emacs

BuildRequires: gcc gcc-c++ cmake git jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel fftw-devel libXt-devel libX11-devel boost-devel alsa-lib-devel
BuildRequires: systemd-devel libatomic avahi-devel qt5-qtlocation-devel qt5-qtsensors-devel
BuildRequires: readline-devel qt5-qtwebengine-devel qt5-qttools-devel
BuildRequires: qt5-qtwebsockets-devel qt5-qtsvg-devel emacs qjackctl ccache

%description
SuperCollider is an object oriented programming environment for
real-time audio and video processing. It is one of the finest and most
versatile environments for signal processing and especially for
creating music applications of all kinds, such as complete
compositions, interactive performances, installations etc.

%package devel
Summary: Development files for SuperCollider
Group: Development/Libraries
Requires: supercollider = %{version}-%{release} pkgconfig
Requires: jack-audio-connection-kit-devel alsa-lib-devel
Requires: libsndfile-devel

%description devel
This package includes include files and libraries neede to develop
SuperCollider applications

%package emacs
Summary: SuperCollider support for Emacs
Group: Applications/Multimedia
Requires: supercollider = %{version}-%{release}

%description emacs
SuperCollider support for the Emacs text editor.

%package gedit
Summary: SuperCollider support for GEdit
Group: Applications/Multimedia
Requires: supercollider = %{version}-%{release}

%description gedit
SuperCollider support for the GEdit text editor.

%package vim
Summary: SuperCollider support for Vim
Group: Applications/Multimedia
Requires: supercollider = %{version}-%{release}

%description vim
SuperCollider support for the Vim text editor.

%prep
%setup -q -n SuperCollider-Source

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_SKIP_RPATH:BOOL=ON ..
make %{?_smp_mflags}
popd

%install
%{__mkdir} -p %{buildroot}

pushd build
make install DESTDIR=%{buildroot}
popd

%files
%doc COPYING README*
%{_bindir}/supernova
%{_bindir}/scide
%{_bindir}/sclang
%{_bindir}/scsynth
%{_libdir}/SuperCollider/plugins
%{_datadir}/SuperCollider/SCClassLibrary
%{_datadir}/SuperCollider/HelpSource
%{_datadir}/SuperCollider/HID_Support
%{_datadir}/SuperCollider/sounds
%{_datadir}/SuperCollider/translations
%{_datadir}/SuperCollider/AUTHORS
%{_datadir}/SuperCollider/CHANGELOG.md
%{_datadir}/SuperCollider/COPYING
%{_datadir}/SuperCollider/README*
%{_datadir}/pixmaps/supercollider*
%{_datadir}/pixmaps/sc_ide.svg
%{_datadir}/applications/SuperColliderIDE.desktop
%{_datadir}/SuperCollider/examples

%files devel
%{_includedir}/SuperCollider

%files emacs
%doc editors/sc-el/README.md
%{_datadir}/emacs/site-lisp/SuperCollider
%{_datadir}/SuperCollider/Extensions/scide_scel

%files vim
%doc editors/scvim/README.md
%{_datadir}/SuperCollider/Extensions/scide_scvim

%files gedit
%doc editors/sced/README.md
%{_libdir}/gedit/plugins/supercollider*
%{_datadir}/gtksourceview*/language-specs/supercollider.lang
%{_datadir}/mime/packages/supercollider.xml

%changelog
* Thu Apr 11 2019 Tristan Cacqueray <tdecacqu@redhat.com> - 3.10.2-1
- Bump to 3.10.2

* Fri Aug 10 2012 Jørn Lomax <northlomax@gmail.com> 3.5.2-1
- initial port to fedora

* Tue Jun 26 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.2-1.fcX.1
- rebuild for fc14 and gedit2

* Wed May  9 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- downloaded Dan Stowell's version of Julius Smith's patch, no change in release

* Tue May  8 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.2-1
- update to 3.5.2 and latest pv ugens fix by Julius Smith

* Mon May  7 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- new version of new pv ugens by Julius Smith (no change in release)

* Sat May  5 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.1-4
- add new pv ugens by Julius Smith

* Fri May  4 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.1-3
- add patch to fix sfft code (Julius Smith)

* Thu Apr 19 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.1-2
- add patch to fix qttextview background

* Mon Apr  2 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.1-1
- update to 3.5.1

* Tue Mar 20 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5.0-1
- update to official 3.5.0 release
- remove the build_supernova flag, always build it

* Sat Mar 17 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120317
- updated to current git for latest fixes

* Thu Mar  1 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120301
- add perl incantation to fix supernova plugin path for x86_64
- update to current 3.5 branch git (should be post-rc3)

* Tue Feb 28 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120228
- update to current 3.5 git to fix boost asio includes
- fix file list, gedit-2 no longer there
- readd libscsynth and libsupercollider_boost_thread libraries, add
  build define to keep the spec file compatible with git HEAD

* Mon Feb 27 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.rc2
- updated to 3.5-rc2 (February 20th)

* Tue Feb 14 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120213
- update to current git
- remove supercollider-sclang package and supercollider-libscsynth,
  these packages were created when sc was not 64 bit compliant so
  we could install a 32 bit sclang on a 64 bit install
- merge supernova package into main package, remove boost library from files
- remove -DSSE42=ON build option (only valid for very new Nehalem processors)
- remove -DSSE41=ON, roundsd does not work even in a Core Duo processor

* Wed Feb  1 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20120201
- updated to current git (20120201)
- libsclang.so* is no longer used, remove from files

* Tue Jan  3 2012 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111230
- libQtCollider.so no longer exists, add qt-webkit-devel build requirement

* Fri Dec 30 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111230
- update to latest git

* Wed Oct 26 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111026
- update to latest git (fix sse initialization)

* Mon Oct 24 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111024
- update to latest git fixes

* Fri Oct 21 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111021
- update to current supercollider git
- remove sc3-plugins, SwingOSC and quarks from build, they are now
  (again) separate packages
- remove very old obsolete and provides

* Wed Oct 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- tons of changes to the spec file

* Tue Oct 18 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111018
- update to latest sc3 and sc3-plugins git (makefile fixes for supernova)

* Sat Oct 15 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- add git version of sc3-plugins, latest swingosc and latest quarks
- package cruciallib for Instr and friends (used to be part of the
  main distribution)

* Fri Oct 14 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.5-0.1.git20111014
- start packaging current supercollider git for supernova support

* Sat Aug 27 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.4.4-1
- new build, supercollider > 3.4 does not come with sc3-plugins
  or swingosc anymore, add those two sources separately as well as
  svn 2002 of the quark repository

* Tue May 31 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.4-2
- added -fpermissive workaround for building on fc15/gcc4.6 (SC_Wii.cpp
  fails to compile). This is of course not a proper fix.

* Sat Jan  8 2011 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.4-2
- add optimizations to plugins build

* Mon Jul 19 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.4-1
- add supercollider-3.4-stknamespace.patch for Fedora 13's gcc

* Fri Jul 16 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.4-1
- update to 3.4, sclang now builds on x86_64
- add libicu and readline build dependencies (readline test fails
  due to - probably - a header problem, so comment the test out and
  assume that readline-devel is installed, patch1)
- rework stkfloat patch for new version

* Tue Jun  8 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-5
- add patch to change MY_FLOAT to StkFloat in stk ugen code, use the
  external include files for stk. Do not use internal header files anymore.

* Fri May 21 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-4
- with newer version of stk in Fedora sc can link dynamically against
  stk

* Mon Mar  8 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-4
- rebuild against newer stk libraries, fails to link at runtime with
  missing symbols (will try with static stk build)

* Fri Jan 22 2010 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-3
- split libscsynth into a separate package so that both 32 and 64 bits
  versions can be installed in a 64 bit environment (the 32 bit version
  is needed by the 32 bit sclang binary).

* Tue Jul 21 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-2
- add patch2 to deal with breakage in gcc4.4/fc11 in swingosc, see
  http://www.listarc.bham.ac.uk/lists/sc-dev/msg10558.html

* Sat Jul  4 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- install to proper lib64 path on x86_64
- add sc scel code to install, SConstruct fails to install it

* Wed Jul  1 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- split out language in supercollider-sclang
- redo all file lists based on manual installs in a mock chroot
- enable builds on x86_64, the supercollider-sclang will be copied
  from the i386 build

* Tue Jun 30 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- split emacs support into separate package
- added ProcMod.sc patch from Josh for extras
- create MathLib, AmbIEM, redUniverse, dewdrop_lib packages from
  quarks source

* Sun Jun 28 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3.1-1
- updated to stable 3.3.1 with Extras
- rework stk.so patch, AY patch included now in source
- rework scvim and sced install

* Fri Jun 12 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3-1
- updated to stable 3.3 with Extras (added Obsoletes/Provides for all
  sc3 related packages
- build and install all sc3-plugins, SwingOSC
- add AY patch PIC to avoid selinux text relocation errors

* Thu Mar 26 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3-0.rc.svn8982.1
- testing 3.3.RC svn

* Mon Mar 16 2009 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.3-0.alpha.svn8939.1
- testing 3.3 alpha, added ruby to build requirements (needed by scvim)
- disable install of scvim until install target is fixed

* Mon Nov 10 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-0.svn7903.1
- add obsoletes/provides for supercollider-beqsuite-ugens

* Sun Nov  9 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-0.svn7903.1
- update to current svn

* Wed Apr 16 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-0.svn7501.4
- build with JACK_DLL enabled and Wii support on on Fedora >= 7
  (needs cwiid-devel package)

* Tue Apr  8 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-0.svn7501.2
- do not use SC_USE_JACK_CLIENT_NEW which is the default, add patch0
  to eliminate the code from SC_Jack.cpp (was it truly on? I should
  double check)

* Sat Apr  5 2008 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.2.1-0.svn7501.1
- updated to current svn
- no longer install /etc/sclang.cfg
- changed version numbering scheme to include the proper version
- /usr/lib/SuperCollider/plugins/ReverbUGens.so conflicts with the
  old supercollider-reverb-ugens collection (built from the
  supercollider-sc3-plugins, also supercollider-ljpc-classes,
  supercollider-dewdrop, supercollider-josh-ugens

* Fri Feb  1 2008 Arnaud Gomes-do-Vale <Arnaud.Gomes@ircam.fr>
- built on CentOS
- won't build on x86_64

* Sat Nov 17 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU>
- installed Headers in the proper location that matches the pkgconfig
  CFLAGS locations

* Tue Jul 24 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU>
- updated to svn from 07.07.23
- added w3m to build and run dependencies
- "source" directory is now "Source"
- added emacs readme file as README.emacs
- fix build on fc7, replace emacs with emacs-22.1

* Tue May  8 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20070219-0.2.5866svn
- build on fc7, add patch0 to direct X11 path to right location

* Thu Mar  8 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20070219-0.2.5866svn
- install all source files in the -devel package, some UGens (sc3-plugins)
  need the full source to build

* Wed Feb 21 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20070219-0.1.5866svn
- updated to svn 5866

* Fri Jan 19 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20070118-0.2.5811svn
- added Platform to /etc/sclang.conf (otherwise linux specific classes
  are not loaded)
- in fc4 remove URL tag from .pc files, the stock pkgconfig does not like
  them (later updates do but the build env does not use them)
- split -devel package, add proper requires (libhowl, avahi)

* Thu Jan 18 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20070118-0.1.5811svn
- switched to svn, updated to revision 5811
- added static scsynth.a lib to files list

* Mon Jan 15 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.1.cvs
- added missing libXt-devel dependency in fc5/6

* Thu Jan 11 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.5.cvs
- build on fc5 and fc6, remove howl-devel dependency as howl is no
  longer being developed or maintained. Replace with Avahi.

* Mon Jan  8 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.5.cvs
- added howl-devel build requirement (erased openmotif-devel)
- fix removal of CVS directories (a directory with spaces in it was
  being erased by mistake)

* Thu Jan  4 2007 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.4.cvs
- updated to cvs snapshot 2007.01.04
- add a line in /etc/sclang.cfg to include ~/.sclang.scel.cfg if exists

* Tue Dec 26 2006 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.4.cvs
- really enable crucial and JITLib (needed \+ instead of just + in
  perl one-liner)

* Tue Dec 19 2006 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.3.cvs
- install SCComplex.h file, Josh Parmenter's PV needs it (and anything
  using FFT_UGens.h)

* Mon Dec 18 2006 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127-0.2.cvs
- enabled crucial and JITlib by default in /etc/sclang.conf

* Mon Nov 27 2006 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20061127
- updated get-cvs script with new urls
- updated to cvs snapshot dated 20061127.105006

* Thu Jan  5 2006 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20060105
- updated to cvs snapshot 2006.01.05

* Fri Jul 15 2005 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU>
- added fc4/gcc4 patch posted by Russell Johnston

* Thu Jul 14 2005 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20050714
- updated to today's cvs
- add scons DEVELOPMENT option to get all the devel files built and
  installed

* Thu Jun 30 2005 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20050630
- updated to cvs snapshot 2005.06.30
- build is now scons based
- added patch for gcc4 build

* Thu May  5 2005 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20050505
- updated to cvs snapshot 2005.05.05
- added howl-devel build requirement on fc3
- create proper configuration file
- do not add ~/supercollider directory, users will need to create the
  proper subdirectories in the current directory before starting sclang

* Sun Oct  3 2004 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20040930
- tried to --enable-lid but compile fails

* Thu Sep 30 2004 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 0.0.20040930
- cvs: 2004/09/30
- added patch to configure to add X11 library path search

* Fri Aug 13 2004 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 2004.08.13-1
- downloaded new cvs snapshot
- many changes to spec file
- add .so.0 links for sclang and scsynth shared libraries

* Wed Jan 21 2004 Fernando Lopez-Lezcano <nando@ccrma.Stanford.EDU> 3.0-1.cvs
- Initial build.
- installs a /root/.sclang.cfg??
