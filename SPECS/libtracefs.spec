Name: libtracefs
Version: 1.8.0
Release: 6%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-2.0-only
Summary: Library for access kernel tracefs

URL: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%{version}.tar.gz
Patch0: libtracefs-Call-va_end-before-exiting-tracefs_hist_s.patch
Patch1: libtracefs-Prevent-memory-leak-in-append_filer.patch
Patch2: libtracefs-Prevent-a-memory-leak-in-update_fields.patch
Patch3: libtracefs-Prevent-a-memory-leak-in-tracefs_synth_ad.patch
Patch4: libtracefs-Prevent-memory-leak-in-tracefs_event_syst.patch
Patch5: libtracefs-Don-t-leak-socket-file-descriptor-in-open.patch
Patch6: libtracefs-Prevent-a-memory-leak-in-add_func_str.patch
Patch7: libtracefs-Prevent-a-memory-leak-in-tracefs_system_e.patch
Patch8: libtracefs-Prevent-a-memory-leak-in-open_cpu_files.patch
Patch9: libtracefs-Prevent-memory-leak-in-tracefs_instance_c.patch
Patch10: libtracefs-my_yyinput-should-return-0-when-no-data-c.patch
Patch11: libtracefs-Prevent-memory-leak-in-tracefs_dynevent_g.patch
Patch12: libtracefs-Close-dir-in-the-error-path-in-tracefs_sy.patch
Patch13: libtracefs-Close-dir-in-the-error-path-in-tracefs_ev.patch
Patch14: libtracefs-Initialize-val-in-build_filter.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libtraceevent) >= 1.8.0
# The libtracefs is meant to be used by perf, trace-cmd etc. in the future, before it's ready in perf, let's add a conflict
Conflicts: trace-cmd < 2.9.1-6

%description
libtracefs is a library for accessing kernel tracefs

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Development headers of %{name}

%prep
%autosetup -p1

%build
%set_build_flags
# parallel compiling don't always work
make -O -j1 V=1 VERBOSE=1 prefix=%{_prefix} libdir=%{_libdir} all

%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
rm -rf %{buildroot}/%{_libdir}/libtracefs.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.8.0

%files devel
%{_includedir}/tracefs/tracefs.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Tue Oct 29 2024 Troy Dawson <tdawson@redhat.com> - 1.8.0-6
- Bump release for October 2024 mass rebuild:
  Resolves: RHEL-64018

* Wed Jul 10 2024 Jerome Marchand <jmarchan@redhat.com> - 1.8.0-5
- Fix SAST vulnerabilities (RHEL-40413)

* Tue Jul 09 2024 Jerome Marchand <jmarchan@redhat.com> - 1.8.0-4
- Build with LTO (RHEL-46715)

* Mon Jun 24 2024 Troy Dawson <tdawson@redhat.com> - 1.8.0-3
- Bump release for June 2024 mass rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Tue Jan 23 2024 Zamir SUN <sztsian@gmail.com> - 1.8.0-1
- Update to 1.8.0 (RHBZ#2213357)

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 05 2023 Zamir SUN <sztsian@gmail.com> - 1.6.4-2
- SPDX migration

* Wed Apr 05 2023 Zamir SUN <sztsian@gmail.com> - 1.6.4-1
- Update to 1.6.4

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 11 2022 Zamir SUN <sztsian@gmail.com> - 1.5.0-1
- Update to 1.5.0

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Apr 15 2022 Zamir SUN <sztsian@gmail.com> - 1.3.1-2
- Update with newer libtracefs

* Wed Apr 13 2022 Zamir SUN <sztsian@gmail.com> - 1.3.1-1
- Update to 1.3.1

* Tue Feb 15 2022 Zamir SUN <sztsian@gmail.com> - 1.2.5-1
- Update to 1.2.5

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild


* Mon Apr 19 2021 Zamir SUN <sztsian@gmail.com> - 1.1.1-1
- Update to 1.1.1

* Wed Mar 24 2021 Jerome Marchand <jmarchan@redhat.com> - 1.0.2-2
- Remove conflict for latest trace-cmd

* Mon Feb 08 2021 Zamir SUN <sztsian@gmail.com> - 1.0.2-1
- Update to 1.0.2

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 0-0.1.20201120git4f24f98
- Initial libtracefs

