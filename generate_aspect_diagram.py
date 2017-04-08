import sys

import pygraphviz as pgv

import coalib.bearlib.aspects

def import_all_subaspects(package_name):
    package = sys.modules[package_name]
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):
        importlib.import_module(package_name + '.' + name)

def iterate_tree(aspect, graph):
	if aspect.subaspects:
		for k, subaspect in aspect.subaspects.items():
			graph.add_edge(aspect.__name__, subaspect.__name__)
			iterate_tree(subaspect, graph)
	return 
	
if __name__ == 'main':
	import_all_subaspects('coalib.bearlib.aspects')

	aspect_tree = pgv.AGraph(directed=True)
	iterate_tree(Root, aspect_tree)
	aspect_tree.layout(prog='dot')
	aspect_tree.draw('aspect_diagram.png')
	