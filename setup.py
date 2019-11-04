from distutils.core import setup
setup(
  name = 'nertivia',         # How you named your package folder (MyLib)
  packages = ['nertivia'],   # Chose the same as "name"
  version = '0.1.4',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python API Wrapper for Nertivia',   # Give a short description about your library
  author = 'Jared Galyan',                   # Type in your name
  author_email = 'jared@cyphernia.com',      # Type in your E-Mail
  url = 'https://github.com/JarDidi/Nertivia.py',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/JarDidi/Nertivia.py/archive/v0.1.4.tar.gz',    # I explain this later on
  keywords = ['API Wrapper', 'SIMPLE', 'PYTHON'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'python-socketio',
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)