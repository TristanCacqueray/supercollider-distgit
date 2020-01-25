# Supercollider fedora packages

## Install

Grab the build from https://copr.fedorainfracloud.org/coprs/tdecacqu/supercollider/


## Rebuild

Use a [podenv](https://github.com/podenv/podenv) `fedora-devel` container, or using a Fedora shell:

```shell
# Install rpmbuild requirements
dnf install -y rpmbuild dnf-utils
# Install supercollider build requirements
dnf builddep -y supercollider.spec

# Fetch the sources
rpmdev-setuptree
spectool -g -C ~/rpmbuild/SOURCES supercollider.spec

# Build the package
rpmbuild -ba supercollider.spec

# Repeat for the plugins
dnf install -y ~/rpmbuild/RPMS/noarch/supercollider-devel* ~/rpmbuild/RPMS/x86_64/supercollider-3*.rpm
dnf builddep -y supercollider-sc3-plugins.spec
spectool -g -C ~/rpmbuild/SOURCES supercollider-sc3-plugins.spec
rpmbuild -ba supercollider-sc3-plugins.spec
```
