#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from setuptools import setup

setup(
  name         = 'TracEnvisionTheme',
  version      = '1.0',
  packages     = ['envisiontheme'],
  package_data = { 'envisiontheme': ['templates/*.html', 'htdocs/*.css', 'htdocs/*' ] },

  author           = 'Danial Pearce',
  author_email     = 'trac-themes@tigris.id.au',
  description      = 'A port of the mephisto theme, Skittlish, created by evil.che.lu.',
  license          = 'BSD',
  keywords         = 'skittlish trac plugin theme',
  url              = 'http://trac-hacks.org/wiki/SkittlishTheme',
  classifiers      = [
    'Framework :: Trac'
  ],
  install_requires = ['Trac>=0.11', 'TracThemeEngine>=2.0'],
  entry_points = {
    'trac.plugins': [
      'envisiontheme.theme = envisiontheme.theme',
    ]
  },
)
