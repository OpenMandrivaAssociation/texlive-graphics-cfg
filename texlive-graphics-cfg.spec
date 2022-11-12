Name:		texlive-graphics-cfg
Version:	41448
Release:	1
Summary:	Standard LaTeX graphics
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/graphics-cfg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-cfg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-cfg.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires:	texlive-graphics
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Default configuration files for the texlive graphicx module

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/graphics-cfg
%doc %{_texmfdistdir}/doc/latex/graphics-cfg

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
