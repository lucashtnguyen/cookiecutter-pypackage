import sys
import matplotlib
matplotlib.use('agg')

import {{ cookiecutter.project_slug }}
status = {{ cookiecutter.project_slug }}.test(*sys.argv[1:])
sys.exit(status)
