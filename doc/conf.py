# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.abspath(cwd))
sys.path.insert(0, os.path.abspath(os.path.join(cwd, '..')))
sys.path.insert(0, os.path.abspath(os.path.join(cwd, '..', 'src')))

# AutoStructify needed for getting full Sphinx features from markdown (.md) files
# https://recommonmark.readthedocs.io/en/latest/auto_structify.html
import recommonmark
from recommonmark.transform import AutoStructify

# mock out imports of non-standard library modules
# NOTE _gdbm is mocked out due to an error encountered in running autodoc on six.py
# with python 3.7 (gdbm is one of the modules covered by six.moves.)
autodoc_mock_imports = ['subprocess32', '_gdbm']
import mock # do this twice just to be safe
for module in autodoc_mock_imports:
    sys.modules[module] = mock.Mock()

# -- Project information -----------------------------------------------------

project = u'MDTF-diagnostics'
copyright = u'2020, Model Diagnostics Task Force'
author = u'Model Diagnostics Task Force'

# The short X.Y version
version = u''
# The full version, including alpha/beta/rc tags
release = u'3.0 beta 1'

# only used for resolving relative links in markdown docs
# use develop branch because that's what readthedocs is configured to use
_project_github_url = 'https://github.com/NOAA-GFDL/MDTF-diagnostics/tree/develop/'

# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'copy_pod_docs',
    'sphinx.ext.autosummary',
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'recommonmark'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [u'_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'default'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'extra_nav_links' : {
        "Getting Started (PDF)": "https://mdtf-diagnostics.readthedocs.io/en/latest/_static/MDTF_getting_started.pdf",
        "Developer's Walkthough (PDF)": "https://mdtf-diagnostics.readthedocs.io/en/latest/_static/MDTF_walkthrough.pdf",
        "Full documentation (PDF)": "https://mdtf-diagnostics.readthedocs.io/_/downloads/en/latest/pdf/"
    }
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# Sphinx automatically copies referenced image files.
html_static_path = ['_static']

# # Paths (filenames) here must be relative to (under) html_static_path as above:
# html_css_files = [
#     'custom.css',
# ]

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
html_sidebars = {
    '**': ['about.html', 'navigation.html', 'relations.html', 'searchbox.html']
}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'MDTF-diagnosticsdoc'


# -- Options for LaTeX output ------------------------------------------------

# pdflatex is default, xelatex recommended for better unicode support
latex_engine = 'xelatex'

# A dictionary that contains LaTeX snippets that override those Sphinx
# usually puts into the generated .tex files.
latex_elements = {
    'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '11pt',
    # fonts
    'fontpkg': r'''
        \usepackage{fontspec}
        % RTD uses a texlive installation on linux; apparently xelatex can only
        % find fonts by filename in this situation.
        \setmainfont{texgyretermes-regular.otf}
        \setsansfont{Heuristica-Bold.otf}
    ''',
    # chapter style
    'fncychap': '\\usepackage[Bjarne]{fncychap}',
    # Latex figure (float) alignment
    'figure_align': 'H',
    # Additional stuff for the LaTeX preamble.
    'preamble': r"""
        \usepackage{unicode-math}
        \makeatletter
        \fancypagestyle{normal}{
            \fancyhf{}
            \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
            % \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
            % \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
            \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}
            \renewcommand{\headrulewidth}{0.4pt}
            \renewcommand{\footrulewidth}{0pt}
        }
        \fancypagestyle{plain}{
            % used for first page of a chapter only
            \fancyhf{}
            \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
            \renewcommand{\footrulewidth}{0pt}
        }
        \makeatother
    """,
    'extraclassoptions': 'openany'
}
# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        # "Main" PDF containing all source files. This is built automatically by
        # ReadTheDocs (filename is fixed by the RTD account name).
        'tex_all', 'mdtf-diagnostics.tex', 
        u'MDTF Diagnostics Documentation', author, 'manual'
    ),(
        # Secondary PDF. Sphinx will build multiple PDFs, but as far as I can 
        # tell, ReadTheDocs won't (linked open issues in prior commits to this 
        # file?). Instead these are currently built manually and checked into 
        # /docs/static_. The ".tex_" extension is to prevent an error in RTD's 
        # build process if it finds multiple .tex files, and doesn't affect sphinx.
        'tex_getting_started', 'MDTF_getting_started.tex_', 
        u"MDTF Getting Started Guide", 
        r"Thomas Jackson (GFDL), Yi-Hung Kuo (UCLA), Dani Coleman (NCAR)", 
        'sphinxmdtfhowto'
    ),(
        # another secondary PDF.
        'tex_walkthrough', 'MDTF_walkthrough.tex_', 
        u"MDTF Developer's Walkthrough", 
        (
        r"Yi-Hung Kuo\textsuperscript{a} \and Dani Coleman\textsuperscript{b} "
        r"\and Thomas Jackson\textsuperscript{c} \and Chih-Chieh (Jack) Chen\textsuperscript{b} "
        r"\and Andrew Gettelman\textsuperscript{b} \and J.~David Neelin\textsuperscript{a} "
        r"\and Eric Maloney\textsuperscript{d} \and John Krasting\textsuperscript{c}"
        r"\\ {\small (a: UCLA; b: NCAR; c: GFDL; d:CSU)}"
        ),
        'sphinxmdtfhowto'
    )
]

latex_additional_files = [
    'latex/sphinxmdtfhowto.cls',
    'latex/latexmkrc'
]

# latex_docclass = {
#     'mdtfhowto': 'mdtfhowto'
# }

latex_logo = 'img/CPO_MAPP_MDTF_Logo.jpg'

# # For "manual" documents, if this is true, then top-level headings are
# # parts, not chapters.
# latex_toplevel_sectioning = 'chapter'

# If true, show page references after internal links.
latex_show_pagerefs = True

# If true, show URL addresses after external links.
latex_show_urls = 'footnote'

# If false, no module index is generated.
latex_domain_indices = True

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'mdtf-diagnostics', u'MDTF-diagnostics Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'MDTF-diagnostics', u'MDTF-diagnostics Documentation',
     author, 'MDTF-diagnostics', 'One line description of project.',
     'Miscellaneous'),
]


# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = project

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# == Extension configuration ==================================================

# -- Autodoc configuration

# set options, see http://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
autodoc_member_order = 'bysource'
autodoc_default_options = {
    'member-order': 'bysource',
    'special-members': '__init__',
    'private-members': False,
    'undoc-members': True,
    'show-inheritance': True
}
# For simplicty, the six.py library is included directly in the /src module, 
# but we don't want to document it.
# https://stackoverflow.com/a/21449475
def autodoc_skip_member(app, what, name, obj, skip, options):
    return skip or ('six' in name)

# generate autodocs by running sphinx-apidoc when evaluated on readthedocs.org.
# source: https://github.com/readthedocs/readthedocs.org/issues/1139#issuecomment-398083449
def run_apidoc(_):
    ignore_paths = []
    argv = ["--force", "--no-toc", "--separate", "-o", "./sphinx", "../src"
        ] + ignore_paths

    try:
        # Sphinx 1.7+
        from sphinx.ext import apidoc
        apidoc.main(argv)
    except ImportError:
        # Sphinx 1.6 (and earlier)
        from sphinx import apidoc
        argv.insert(0, apidoc.__file__)
        apidoc.main(argv)

# -- Extensions to the Napoleon GoogleDocstring class ---------------------
# copied from: https://michaelgoerz.net/notes/extending-sphinx-napoleon-docstring-sections.html
# purpose: provide correct formatting of class attributes when documented 
# with Google-style docstrings.

from sphinx.ext.napoleon.docstring import GoogleDocstring

# first, we define new methods for any new sections and add them to the class
def parse_keys_section(self, section):
    return self._format_fields('Keys', self._consume_fields())
GoogleDocstring._parse_keys_section = parse_keys_section

def parse_attributes_section(self, section):
    return self._format_fields('Attributes', self._consume_fields())
GoogleDocstring._parse_attributes_section = parse_attributes_section

def parse_class_attributes_section(self, section):
    return self._format_fields('Class Attributes', self._consume_fields())
GoogleDocstring._parse_class_attributes_section = parse_class_attributes_section

# we now patch the parse method to guarantee that the the above methods are
# assigned to the _section dict
def patched_parse(self):
    self._sections['keys'] = self._parse_keys_section
    self._sections['class attributes'] = self._parse_class_attributes_section
    self._unpatched_parse()
GoogleDocstring._unpatched_parse = GoogleDocstring._parse
GoogleDocstring._parse = patched_parse

# -- Options for intersphinx extension -----------------------------------------
intersphinx_mapping = {'python': ('https://docs.python.org/3.7', None)}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# == Overall Sphinx app setup hook =============================================

def setup(app):
    # register autodoc events
    app.connect('builder-inited', run_apidoc)
    app.connect('autodoc-skip-member', autodoc_skip_member)

    # AutoStructify for recommonmark
    # see eg https://stackoverflow.com/a/52430829
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: _project_github_url + url,
        'enable_auto_toc_tree': False,
        'enable_math': True,
        'enable_inline_math': True,
        'enable_eval_rst': True
        # 'enable_auto_doc_ref': True, # deprecated, now default behavior
    }, True)
    app.add_transform(AutoStructify)
