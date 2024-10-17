Name:		texlive-chifoot
Version:	57312
Release:	2
Summary:	Chicago-style footnote formatting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/chifoot
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chifoot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/chifoot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A very short snippet. Will set the footnotes to be conformant
with the Chicago style, so the footnotes at the bottom of the
page are now marked with a full-sized number, rather than with
a superscript number.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/chifoot
%doc %{_texmfdistdir}/doc/latex/chifoot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
