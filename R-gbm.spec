#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-gbm
Version  : 2.1.8
Release  : 39
URL      : https://cran.r-project.org/src/contrib/gbm_2.1.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/gbm_2.1.8.tar.gz
Summary  : Generalized Boosted Regression Models
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: R-gbm-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
algorithm and Friedman's gradient boosting machine. Includes regression 
  methods for least squares, absolute loss, t-distribution loss, quantile 
  regression, logistic, multinomial logistic, Poisson, Cox proportional hazards 
  partial likelihood, AdaBoost exponential loss, Huberized hinge loss, and 
  Learning to Rank measures (LambdaMart). Originally developed by Greg Ridgeway.

%package lib
Summary: lib components for the R-gbm package.
Group: Libraries

%description lib
lib components for the R-gbm package.


%prep
%setup -q -c -n gbm
cd %{_builddir}/gbm

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1594829795

%install
export SOURCE_DATE_EPOCH=1594829795
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
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbm
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library gbm
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc gbm || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/gbm/DESCRIPTION
/usr/lib64/R/library/gbm/INDEX
/usr/lib64/R/library/gbm/LICENSE
/usr/lib64/R/library/gbm/Meta/Rd.rds
/usr/lib64/R/library/gbm/Meta/demo.rds
/usr/lib64/R/library/gbm/Meta/features.rds
/usr/lib64/R/library/gbm/Meta/hsearch.rds
/usr/lib64/R/library/gbm/Meta/links.rds
/usr/lib64/R/library/gbm/Meta/nsInfo.rds
/usr/lib64/R/library/gbm/Meta/package.rds
/usr/lib64/R/library/gbm/Meta/vignette.rds
/usr/lib64/R/library/gbm/NAMESPACE
/usr/lib64/R/library/gbm/NEWS.md
/usr/lib64/R/library/gbm/R/gbm
/usr/lib64/R/library/gbm/R/gbm.rdb
/usr/lib64/R/library/gbm/R/gbm.rdx
/usr/lib64/R/library/gbm/demo/OOB-reps.R
/usr/lib64/R/library/gbm/demo/bernoulli.R
/usr/lib64/R/library/gbm/demo/coxph.R
/usr/lib64/R/library/gbm/demo/gaussian.R
/usr/lib64/R/library/gbm/demo/multinomial.R
/usr/lib64/R/library/gbm/demo/pairwise.R
/usr/lib64/R/library/gbm/demo/printExamples.R
/usr/lib64/R/library/gbm/demo/robustReg.R
/usr/lib64/R/library/gbm/doc/gbm.Rnw
/usr/lib64/R/library/gbm/doc/gbm.pdf
/usr/lib64/R/library/gbm/doc/index.html
/usr/lib64/R/library/gbm/help/AnIndex
/usr/lib64/R/library/gbm/help/aliases.rds
/usr/lib64/R/library/gbm/help/gbm.rdb
/usr/lib64/R/library/gbm/help/gbm.rdx
/usr/lib64/R/library/gbm/help/paths.rds
/usr/lib64/R/library/gbm/html/00Index.html
/usr/lib64/R/library/gbm/html/R.css
/usr/lib64/R/library/gbm/tests/tinytest.R
/usr/lib64/R/library/gbm/tinytest/test_bernoulli.R
/usr/lib64/R/library/gbm/tinytest/test_coxph.R
/usr/lib64/R/library/gbm/tinytest/test_least_squares.R
/usr/lib64/R/library/gbm/tinytest/test_relative_influence.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/gbm/libs/gbm.so
/usr/lib64/R/library/gbm/libs/gbm.so.avx2
/usr/lib64/R/library/gbm/libs/gbm.so.avx512
