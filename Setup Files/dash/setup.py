import os
import shutil
import sys
import zipfile
import platform

from distutils.core import setup, Extension
from distutils.sysconfig import get_python_lib
import py2exe

version = str('1.4+')+str(__import__('p2pool').__version__)
im64 = '64' in platform.architecture()[0]

extra_includes = []
import p2pool.dash
import p2pool.networks
extra_includes.extend('p2pool.networks.' + x for x in p2pool.networks.nets)
import p2pool.dash.networks
extra_includes.extend('p2pool.dash.networks.' + x for x in p2pool.dash.networks.nets)

keccak_hash_module = Extension('keccak_hash',
                                 sources = ['keccakmodule.c',
                                            'keccakhash.c',
                                            'sha3/keccak.c'],
                               include_dirs=['.', './sha3'])

setup (name = 'keccak_hash',
       version = '1.4',
       author = 'rc125',
  	   author_email = 'rc125@protonmail.com',
  	   url = 'https://github.com/rc125/python-keccak_hash',
       description = 'Binding for keccak proof of work hashing.',
       ext_modules = [keccak_hash_module])

if os.path.exists('INITBAK'):
    os.remove('INITBAK')
os.rename(os.path.join('p2pool', '__init__.py'), 'INITBAK')
try:
    open(os.path.join('p2pool', '__init__.py'), 'wb').write('__version__ = %r%s%sDEBUG = False%s' % (version, os.linesep, os.linesep, os.linesep))
    mfcdir = get_python_lib() + '\pythonwin\\'
    mfcfiles = [os.path.join(mfcdir, i) for i in ["mfc90.dll", "mfc90u.dll", "mfcm90.dll", "mfcm90u.dll", "Microsoft.VC90.MFC.manifest"]]
    bundle = 1
    if im64:
        bundle = bundle + 2
    sys.argv[1:] = ['py2exe']
    setup(name='p2pool-dash',
        version=version,
        description='Peer-to-peer Dash mining pool',
        author='Forrest Voight',
        author_email='forrest@forre.st',
        url='https://github.com/dashpay/p2pool-dash/',
        data_files=[
            ('', ['README.md']),
#            ("Microsoft.VC90.MFC", mfcfiles),
            ('web-static', [
                'web-static/d3.v2.min.js',
                'web-static/favicon.ico',
                'web-static/graphs.html',
                'web-static/index.html',
                'web-static/share.html',
            ]),
        ],

        console=['run_p2pool.py'],
        options=dict(py2exe=dict(
            bundle_files=bundle,
            dll_excludes=['w9xpopen.exe', "mswsock.dll", "MSWSOCK.dll"],
            includes=['twisted.web.resource', 
                      'dash_hash',
                      'zope.interface',
                      'win32api',
                      'p2pool.dash',
                     ] + extra_includes,
        )),
        zipfile=None,
    )
finally:
    os.remove(os.path.join('p2pool', '__init__.py'))
    os.rename('INITBAK', os.path.join('p2pool', '__init__.py'))

win = '32'
if im64:
    win = '64'

dir_name = 'p2pool_dash_win' + win + '_' + version

if os.path.exists(dir_name):
    shutil.rmtree(dir_name)

with zipfile.ZipFile(dir_name + '.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
    for dirpath, dirnames, filenames in os.walk('dist'):
        for filename in filenames:
            zf.write(os.path.join(dirpath, filename))

os.rename(dir_name + '.zip', os.path.join('dist',dir_name + '.zip'))

print (dir_name)
