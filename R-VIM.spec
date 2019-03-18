#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-VIM
Version  : 4.8.0
Release  : 19
URL      : https://cran.r-project.org/src/contrib/VIM_4.8.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/VIM_4.8.0.tar.gz
Summary  : Visualization and Imputation of Missing Values
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-VIM-lib = %{version}-%{release}
Requires: R-DEoptimR
Requires: R-car
Requires: R-cellranger
Requires: R-forcats
Requires: R-hms
Requires: R-lmtest
Requires: R-zip
BuildRequires : R-DEoptimR
BuildRequires : R-abind
BuildRequires : R-car
BuildRequires : R-carData
BuildRequires : R-cellranger
BuildRequires : R-colorspace
BuildRequires : R-data.table
BuildRequires : R-e1071
BuildRequires : R-forcats
BuildRequires : R-hms
BuildRequires : R-laeken
BuildRequires : R-lmtest
BuildRequires : R-ranger
BuildRequires : R-rio
BuildRequires : R-robustbase
BuildRequires : R-sp
BuildRequires : R-vcd
BuildRequires : R-zip
BuildRequires : buildreq-R

%description
[![Coverage Status](https://coveralls.io/repos/github/statistikat/VIM/badge.svg?branch=master)](https://coveralls.io/github/statistikat/VIM?branch=master)
[![CRAN](http://www.r-pkg.org/badges/version/VIM)](https://CRAN.R-project.org/package=VIM)
[![Downloads](http://cranlogs.r-pkg.org/badges/VIM)](https://CRAN.R-project.org/package=VIM)
[![Mentioned in Awesome Official Statistics ](https://awesome.re/mentioned-badge.svg)](http://www.awesomeofficialstatistics.org)

%package lib
Summary: lib components for the R-VIM package.
Group: Libraries

%description lib
lib components for the R-VIM package.


%prep
%setup -q -c -n VIM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552920819

%install
export SOURCE_DATE_EPOCH=1552920819
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VIM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VIM
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library VIM
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc  VIM || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/VIM/CITATION
/usr/lib64/R/library/VIM/DESCRIPTION
/usr/lib64/R/library/VIM/INDEX
/usr/lib64/R/library/VIM/Meta/Rd.rds
/usr/lib64/R/library/VIM/Meta/data.rds
/usr/lib64/R/library/VIM/Meta/features.rds
/usr/lib64/R/library/VIM/Meta/hsearch.rds
/usr/lib64/R/library/VIM/Meta/links.rds
/usr/lib64/R/library/VIM/Meta/nsInfo.rds
/usr/lib64/R/library/VIM/Meta/package.rds
/usr/lib64/R/library/VIM/NAMESPACE
/usr/lib64/R/library/VIM/NEWS
/usr/lib64/R/library/VIM/R/VIM
/usr/lib64/R/library/VIM/R/VIM.rdb
/usr/lib64/R/library/VIM/R/VIM.rdx
/usr/lib64/R/library/VIM/data/Rdata.rdb
/usr/lib64/R/library/VIM/data/Rdata.rds
/usr/lib64/R/library/VIM/data/Rdata.rdx
/usr/lib64/R/library/VIM/help/AnIndex
/usr/lib64/R/library/VIM/help/VIM.rdb
/usr/lib64/R/library/VIM/help/VIM.rdx
/usr/lib64/R/library/VIM/help/aliases.rds
/usr/lib64/R/library/VIM/help/paths.rds
/usr/lib64/R/library/VIM/html/00Index.html
/usr/lib64/R/library/VIM/html/R.css
/usr/lib64/R/library/VIM/tests/testthat.R
/usr/lib64/R/library/VIM/tests/testthat/Rplots.pdf
/usr/lib64/R/library/VIM/tests/testthat/test_IRMI_ordered.R
/usr/lib64/R/library/VIM/tests/testthat/test_data_frame.R
/usr/lib64/R/library/VIM/tests/testthat/test_gowerDind.R
/usr/lib64/R/library/VIM/tests/testthat/test_graphics.R
/usr/lib64/R/library/VIM/tests/testthat/test_hotdeck.R
/usr/lib64/R/library/VIM/tests/testthat/test_impNA.R
/usr/lib64/R/library/VIM/tests/testthat/test_kNN.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/VIM/libs/VIM.so
/usr/lib64/R/library/VIM/libs/VIM.so.avx2
/usr/lib64/R/library/VIM/libs/VIM.so.avx512
