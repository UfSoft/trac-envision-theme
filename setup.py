#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 et

from setuptools import setup

setup(
  name         = 'TracEnvisionTheme',
  version      = '1.0',
  packages     = ['envisiontheme'],
  package_data = { 'envisiontheme': [
                    'templates/*.html',
                    'htdocs/*.css',
                    'htdocs/imgs/*.png',
                    'htdocs/imgs/*.gif']},
  author        = 'Pedro Algarvio',
  author_email  = 'ufs@ufsoft.org',
  description   = 'A port of the Envision theme, created by Erwin Aligam.',
  license       = 'BSD',
  keywords      = 'envision trac plugin theme',
  url           = 'https://hg.ufsoft.org/TracEnvisionTheme/',
  classifiers   = [
    'Framework :: Trac'
  ],
  install_requires = ['Trac>=0.11', 'TracThemeEngine>=2.0'],
  entry_points = {
    'trac.plugins': [
      'envisiontheme.theme = envisiontheme.theme',
    ]
  },
)
