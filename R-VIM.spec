#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-VIM
Version  : 6.2.2
Release  : 59
URL      : https://cran.r-project.org/src/contrib/VIM_6.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/VIM_6.2.2.tar.gz
Summary  : Visualization and Imputation of Missing Values
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-VIM-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-car
Requires: R-colorspace
Requires: R-data.table
Requires: R-e1071
Requires: R-laeken
Requires: R-magrittr
Requires: R-ranger
Requires: R-robustbase
Requires: R-sp
Requires: R-vcd
BuildRequires : R-Rcpp
BuildRequires : R-car
BuildRequires : R-colorspace
BuildRequires : R-data.table
BuildRequires : R-e1071
BuildRequires : R-laeken
BuildRequires : R-magrittr
BuildRequires : R-ranger
BuildRequires : R-robustbase
BuildRequires : R-sp
BuildRequires : R-vcd
BuildRequires : buildreq-R

%description
are introduced, which can be used for exploring the data and the structure of
    the missing and/or imputed values. Depending on this structure of the missing
    values, the corresponding methods may help to identify the mechanism generating
    the missing values and allows to explore the data including missing values.
    In addition, the quality of imputation can be visually explored using various
    univariate, bivariate, multiple and multivariate plot methods. A graphical user
    interface available in the separate package VIMGUI allows an easy handling of
    the implemented plot methods.

%package lib
Summary: lib components for the R-VIM package.
Group: Libraries

%description lib
lib components for the R-VIM package.


%prep
%setup -q -n VIM
cd %{_builddir}/VIM

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1661446296

%install
export SOURCE_DATE_EPOCH=1661446296
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :


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
/usr/lib64/R/library/VIM/Meta/vignette.rds
/usr/lib64/R/library/VIM/NAMESPACE
/usr/lib64/R/library/VIM/NEWS.md
/usr/lib64/R/library/VIM/R/VIM
/usr/lib64/R/library/VIM/R/VIM.rdb
/usr/lib64/R/library/VIM/R/VIM.rdx
/usr/lib64/R/library/VIM/data/Rdata.rdb
/usr/lib64/R/library/VIM/data/Rdata.rds
/usr/lib64/R/library/VIM/data/Rdata.rdx
/usr/lib64/R/library/VIM/doc/VIM.R
/usr/lib64/R/library/VIM/doc/VIM.Rmd
/usr/lib64/R/library/VIM/doc/VIM.html
/usr/lib64/R/library/VIM/doc/VisualImp.R
/usr/lib64/R/library/VIM/doc/VisualImp.Rmd
/usr/lib64/R/library/VIM/doc/VisualImp.html
/usr/lib64/R/library/VIM/doc/donorImp.R
/usr/lib64/R/library/VIM/doc/donorImp.Rmd
/usr/lib64/R/library/VIM/doc/donorImp.html
/usr/lib64/R/library/VIM/doc/index.html
/usr/lib64/R/library/VIM/doc/irmi.R
/usr/lib64/R/library/VIM/doc/irmi.Rmd
/usr/lib64/R/library/VIM/doc/irmi.html
/usr/lib64/R/library/VIM/doc/modelImp.R
/usr/lib64/R/library/VIM/doc/modelImp.Rmd
/usr/lib64/R/library/VIM/doc/modelImp.html
/usr/lib64/R/library/VIM/help/AnIndex
/usr/lib64/R/library/VIM/help/VIM.rdb
/usr/lib64/R/library/VIM/help/VIM.rdx
/usr/lib64/R/library/VIM/help/aliases.rds
/usr/lib64/R/library/VIM/help/paths.rds
/usr/lib64/R/library/VIM/html/00Index.html
/usr/lib64/R/library/VIM/html/R.css
/usr/lib64/R/library/VIM/tests/tinytest.R
/usr/lib64/R/library/VIM/tinytest/test_IRMI_ordered.R
/usr/lib64/R/library/VIM/tinytest/test_aggFunctions.R
/usr/lib64/R/library/VIM/tinytest/test_data_frame.R
/usr/lib64/R/library/VIM/tinytest/test_gowerDind.R
/usr/lib64/R/library/VIM/tinytest/test_graphics.R
/usr/lib64/R/library/VIM/tinytest/test_hotdeck.R
/usr/lib64/R/library/VIM/tinytest/test_impNA.R
/usr/lib64/R/library/VIM/tinytest/test_impPCA.R
/usr/lib64/R/library/VIM/tinytest/test_irmi_types.R
/usr/lib64/R/library/VIM/tinytest/test_kNN.R
/usr/lib64/R/library/VIM/tinytest/test_kNN_exact.R
/usr/lib64/R/library/VIM/tinytest/test_kNN_iqr.R
/usr/lib64/R/library/VIM/tinytest/test_kNN_ordered.R
/usr/lib64/R/library/VIM/tinytest/test_rangerImpute.R
/usr/lib64/R/library/VIM/tinytest/test_regressionImp.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/VIM/libs/VIM.so
/usr/lib64/R/library/VIM/libs/VIM.so.avx2
/usr/lib64/R/library/VIM/libs/VIM.so.avx512
