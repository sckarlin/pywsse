# Makefile for the pip-tools managed requirements files

# This variable can be overridden on the make command line
PYTHON = python

# Local PyPI Repository Configuration
#    Setting LOCAL_PIPY_REPO will enable a local PyPI repository
#    If this local repository requires authentication, set NETRC to .netrc
#LOCAL_PYPI_REPO = https://versions.cs.princeton.edu/api/v4/projects/43/packages/pypi/simple
#NETRC = .netrc

PYPROJECT_TOML = ../pyproject.toml

IN_VENV := $(shell $(PYTHON) -c "import sys; print(sys.prefix != sys.base_prefix)")
ifneq ($(IN_VENV),True)
$(error Not in a venv)
endif

ifeq (,$(wildcard $(PYPROJECT_TOML)))
  $(error "$(PYPROJECT_TOML)" does not exist.)
endif

# Security Note:  We search the local repository first with --index-url
# before PyPI with --extra-index-url.  Note that the highest numbered
# version of a package that matches the requirement will be pulled from either
# repository regardless of search order.  However, when both repositories
# have the same highest match, the --index-url repo will be used.  Therefore,
# we must use pinned versions for packages in local repositories.  Otherwise,
# a bad actor could upload a same-named library to PyPI with a higher matching
# version number which would get used in place of our local package.
ifdef LOCAL_PYPI_REPO
  INDEX_URLS = --index-url=$(LOCAL_PYPI_REPO) --extra-index-url=https://pypi.org/simple
else
  INDEX_URLS =
endif

ifdef NETRC
  ifeq (,$(wildcard $(NETRC)))
    $(error NETRC defined as "$(NETRC)" but file does not exist.)
  endif
  PREFIX = NETRC=$(NETRC)
else
  PREFIX =
endif

# --allow-unsafe will be the new default.  Using it is safer than not.
PIP_COMPILE = $(PREFIX) $(PYTHON) -m piptools compile -v --strip-extras --allow-unsafe --generate-hashes $(INDEX_URLS)
PIP_SYNC    = $(PREFIX) $(PYTHON) -m piptools sync -v $(INDEX_URLS)
PIP_SELF    = $(PREFIX) $(PYTHON) -m pip install ../tigeruhr
PIP_SELF_E  = $(PREFIX) $(PYTHON) -m pip install -e . --config-settings editable_mode=strict

PY_MAJOR := $(shell $(PYTHON) -c "import sys; print(sys.version_info.major)")
PY_MINOR := $(shell $(PYTHON) -c "import sys; print(sys.version_info.minor)")

PY_NAME = py$(PY_MAJOR)$(PY_MINOR)


.PHONY: all init sync_devci sync_deploy deploy devci

# Use alternate prefix as PyCharm editor doesn't handle tab characters well
# .RECIPEPREFIX = >

all: init $(PY_NAME)_base.txt $(PY_NAME)_devci.txt

init:
	$(PYTHON) -m pip install --upgrade pip wheel setuptools pip-tools

$(PY_NAME)_base.txt: $(PYPROJECT_TOML)
	rm -f $@
	CUSTOM_COMPILE_COMMAND="make $@" $(PIP_COMPILE) --output-file $@ $<

$(PY_NAME)_devci.txt: $(PYPROJECT_TOML)
	rm -f $@
	CUSTOM_COMPILE_COMMAND="make $@" $(PIP_COMPILE) --output-file $@ --extra devci $<

sync_deploy: $(PY_NAME)_base.txt
	$(PIP_SYNC) $^

sync_devci: $(PY_NAME)_base.txt $(PY_NAME)_devci.txt
	$(PIP_SYNC) $^

deploy: sync_deploy
	$(PIP_SELF)

devci: sync_devci
	(cd .. ; $(PIP_SELF_E))

build:
	(cd .. ; python -m build)
