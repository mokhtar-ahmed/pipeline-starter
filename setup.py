from setuptools import setup
import pk_info as pk



setup(
    name=pk.pack_name,
    use_scm_version=pk.version_info,
    setup_requires=['setuptools_scm'],
    description='sample spark pipeline ci/cd',
    packages=['src.main', 'src.test']
)
