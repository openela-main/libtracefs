# git tag
#%%global commit 4f24f98960c223e56329519bb90a90f0b2ad813f
#%%global commitdate 20201120
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})

# LTO causes linking issues randomly like
# lto1: internal compiler error: resolution sub id 0x7136344381f3059f not in object file
# So disabling LTO at this moment.

%global _lto_cflags %nil

Name: libtracefs
Version: 1.3.1
Release: 2%{?dist}
License: LGPLv2+ and GPLv2+
Summary: Library for access kernel tracefs

URL: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/
# If upstream does not provide tarballs, to generate:
# git clone git://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git
# cd libtracefs
# git archive --prefix=libtracefs-%%{version}/ -o libtracefs-%%{version}.tar.gz %%{git_commit}
#Source0: libtracefs-%%{version}.tar.gz
#Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%%{commit}.tar.gz
Source0: https://git.kernel.org/pub/scm/libs/libtrace/libtracefs.git/snapshot/libtracefs-%{version}.tar.gz
Patch0:  libtracefs-1.0.2-harden-linking.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(libtraceevent)

%description
libtracefs is a library for accessing kernel tracefs

%package devel
Summary: Development headers of %{name}
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
Development headers of %{name}

%prep
%setup -q
%patch0 -p1

%build
%set_build_flags
export GCCLDFLAGS="-Wl,-z,now"
%make_build prefix=%{_prefix} libdir=%{_libdir} all 

%install
%set_build_flags
export GCCLDFLAGS="-Wl,-z,now"
%make_install prefix=%{_prefix} libdir=%{_libdir}
rm -rf %{buildroot}/%{_libdir}/libtracefs.a

%files
%license LICENSES/LGPL-2.1
%license LICENSES/GPL-2.0
%{_libdir}/%{name}.so.1
%{_libdir}/%{name}.so.1.3.1

%files devel
%{_includedir}/tracefs/tracefs.h
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/%{name}.so

%changelog
* Thu Feb 2 2023 Michael Petlan <mpetlan@redhat.com> - 1.3.1-2
- Remove conflict with trace-cmd
  Related: rhbz#2159965

* Mon Nov 23 2020 Zamir SUN <sztsian@gmail.com> - 1.3.1-1
- Initial libtracefs
  Related: rhbz#2075198
