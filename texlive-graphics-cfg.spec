%global tl_name graphics-cfg
%global tl_revision 41448

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Sample configuration files for LaTeX color and graphics
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/graphics-cfg
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-cfg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/graphics-cfg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This bundle includes color.cfg and graphics.cfg files that set default
"driver" options for the color and graphics packages. It contains
support for defaulting the new LuaTeX option which was added to graphics
and color in the 2016-02-01 release. The LuaTeX option is only used for
LuaTeX versions from 0.87, older versions use the pdfTeX option as
before.

