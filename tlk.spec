Summary:	LDP Linux Kernel
Summary(pl.UTF-8):   Przewodnik po kernelu
Name:		tlk
Version:	0.8_3
Release:	1
License:	distributable
Group:		Documentation
Source0:	http://www.tldp.org/LDP/%{name}.html.tar.gz
# Source0-md5:	00df6ba5eaa312e45625aae8cad80d76
URL:		http://www.tldp.org/LDP/tlk/tlk.html
Requires:	LDP-base
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kernel is at the heart of the operating system. This book is a
guide to how the kernel fits together, how it works; a tour of the
kernel.

%description -l pl.UTF-8
Kernel jest sercem systemu operacyjnego. W tej książce opisano jak
działa kernel Linuksa.

%prep
%setup -q -n %{name}-0.8-3.html

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}
cp -a * $RPM_BUILD_ROOT%{_docdir}/LDP/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_docdir}/LDP/%{name}
