# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: php-codesniffer
Epoch: 100
Version: 3.7.1
Release: 1%{?dist}
BuildArch: noarch
Summary: PHP coding standards enforcement tool
License: BSD-2-Clause
URL: https://github.com/squizlabs/PHP_CodeSniffer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
Provides: phpcbf = %{epoch}:%{version}-%{release}
Provides: phpcs = %{epoch}:%{version}-%{release}

%description
PHP_CodeSniffer provides functionality to verify that code conforms to
certain standards, such as PEAR, or user-defined.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%install
install -Dpm755 -d %{buildroot}%{_bindir}
install -Dpm755 -d %{buildroot}%{_datadir}/php/vendor
cp -rfT vendor %{buildroot}%{_datadir}/php/vendor
pushd %{buildroot}/usr/bin && \
    ln -fs %{_datadir}/php/vendor/php-codesniffer/bin/phpcbf phpcbf && \
    ln -fs %{_datadir}/php/vendor/php-codesniffer/bin/phpcs phpcs && \
    popd
chmod a+x %{buildroot}%{_datadir}/php/vendor/php-codesniffer/bin/phpcbf
chmod a+x %{buildroot}%{_datadir}/php/vendor/php-codesniffer/bin/phpcs
fdupes -qnrps %{buildroot}%{_datadir}/php/vendor

%check

%files
%license licence.txt
%dir %{_datadir}/php
%dir %{_datadir}/php/vendor
%{_bindir}/*
%{_datadir}/php/vendor/*


%changelog
