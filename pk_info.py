from setuptools_scm.version import get_no_local_node
from setuptools_scm import get_version, Version, version_from_scm


def clean_scheme(version):
    return get_no_local_node(version)


version_info = {'local_scheme': clean_scheme,
                'write_to': 'src/main/__version__.py'}

vr = get_version()
print(vr)

pack_name = "pipeline"

if "dev" in vr.lower():
    pack_name = "pipeline-snapshot"
